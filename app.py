from flask import Flask, jsonify, request, send_file
import instaloader
import requests
from datetime import timezone
from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED
from urllib.parse import urlparse
import re
import threading

app = Flask(__name__, static_folder="static", static_url_path="")
media_cache = {}
cache_lock = threading.Lock()

def get_username(value):
    value = (value or "").strip()
    if not value:
        raise ValueError("Instagram profil adresini gir.")
    if "://" not in value:
        value = "https://www.instagram.com/" + value.lstrip("@/")
    parsed = urlparse(value)
    if parsed.netloc.lower() not in ("instagram.com", "www.instagram.com"):
        raise ValueError("Instagram profil adresi gir.")
    parts = [p for p in parsed.path.split("/") if p]
    if not parts or parts[0] in ("p", "reel", "reels", "stories", "explore"):
        raise ValueError("Profil bağlantısı geçerli görünmüyor.")
    username = parts[0].lstrip("@")
    if not re.fullmatch(r"[A-Za-z0-9._]{1,30}", username):
        raise ValueError("Kullanıcı adı geçersiz.")
    return username

@app.get("/")
def index():
    return app.send_static_file("index.html")

@app.get("/api/health")
def health():
    return jsonify({"ok": True})

@app.post("/api/profile")
def get_profile():
    try:
        payload = request.get_json(silent=True) or {}
        username = get_username(payload.get("profile"))
        loader = instaloader.Instaloader(
            quiet=True, download_pictures=False, download_videos=False,
            download_video_thumbnails=False, save_metadata=False,
            compress_json=False, max_connection_attempts=2
        )
        profile = instaloader.Profile.from_username(loader.context, username)
        found = []
        new_cache = {}
        for post in profile.get_posts():
            date = post.date_utc.replace(tzinfo=timezone.utc).isoformat()
            if post.typename == "GraphSidecar":
                try:
                    nodes = post.get_sidecar_nodes()
                except Exception:
                    continue
                for number, node in enumerate(nodes, start=1):
                    if getattr(node, "is_video", False):
                        continue
                    url = getattr(node, "display_url", None)
                    if not url:
                        continue
                    media_id = f"{post.shortcode}-{number}"
                    item = {"id": media_id, "date": date, "url": url,
                            "shortcode": post.shortcode, "position": number}
                    found.append(item)
                    new_cache[media_id] = item
            elif not post.is_video:
                media_id = f"{post.shortcode}-1"
                item = {"id": media_id, "date": date, "url": post.url,
                        "shortcode": post.shortcode, "position": 1}
                found.append(item)
                new_cache[media_id] = item
        found.sort(key=lambda x: (x["date"], x["shortcode"], x["position"]))
        with cache_lock:
            media_cache.clear()
            media_cache.update(new_cache)
        return jsonify({"username": profile.username, "count": len(found), "posts": found})
    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({"error": "Profil bulunamadı veya erişilebilir değil."}), 404
    except instaloader.exceptions.ConnectionException as exc:
        return jsonify({"error": "Instagram erişimi sınırladı. Daha sonra tekrar dene. " + str(exc)}), 429
    except Exception as exc:
        return jsonify({"error": "Fotoğraflar alınamadı: " + str(exc)}), 502

@app.post("/api/download")
def download():
    payload = request.get_json(silent=True) or {}
    ids = payload.get("ids") or []
    if not isinstance(ids, list) or not ids:
        return jsonify({"error": "Önce fotoğraf seç."}), 400
    with cache_lock:
        selected = [media_cache[item_id] for item_id in ids if item_id in media_cache]
    if len(selected) != len(set(ids)):
        return jsonify({"error": "Fotoğraf listesi artık geçerli değil. Profili yeniden getir."}), 400
    selected.sort(key=lambda x: (x["date"], x["shortcode"], x["position"]))
    output = BytesIO()
    sequence = 0
    try:
        with ZipFile(output, "w", ZIP_DEFLATED) as archive:
            session = requests.Session()
            session.headers["User-Agent"] = "Mozilla/5.0"
            for item in selected:
                response = session.get(item["url"], timeout=30)
                response.raise_for_status()
                year, month, _ = item["date"][:10].split("-")
                key = f"{month}_{year}"
                sequence += 1
                mime = response.headers.get("Content-Type", "").lower()
                ext = "png" if "png" in mime else "webp" if "webp" in mime else "jpg"
                archive.writestr(f"{key}_{sequence:03d}.{ext}", response.content)
        output.seek(0)
        return send_file(output, mimetype="application/zip", as_attachment=True,
                         download_name="instagram-arsiv.zip")
    except Exception as exc:
        return jsonify({"error": "ZIP hazırlanamadı: " + str(exc)}), 502

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
