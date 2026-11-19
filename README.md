# Instagram Arşivleyici

Mac üzerinde yerel çalışan, herkese açık Instagram profillerindeki fotoğrafları listeleyip seçilenleri ZIP olarak indirmeyi deneyen uygulama.

## Mac'te başlatma

1. Bu repository'yi bilgisayarına ZIP olarak indir ve klasörü aç.
2. `Baslat.command` dosyasına çift tıkla. macOS güvenlik uyarısı verirse dosyaya sağ tıklayıp Aç'ı seç.
3. İlk çalıştırmada gerekli Python paketleri kurulur ve tarayıcıda `http://127.0.0.1:5050` açılır.
4. Instagram profil adresini gir, fotoğrafları listele, seç ve ZIP indir.

Alternatif olarak Terminal'de:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Özellikler

- Açık profil gönderilerini listelemeyi dener.
- Fotoğraf carousel öğelerini ayrı gösterir; videoları atlar.
- Tarihe göre sıralar, tek tek veya tümünü seçtirir.
- ZIP dosya adlarını ay-yıl-sıra biçiminde oluşturur: `11_2026_001.jpg`.

## Sınırlamalar

Instagram üçüncü taraf erişimini değiştirebilir, istekleri sınırlayabilir veya bazı/eski gönderileri döndürmeyebilir. Tüm gönderilerin alınması garanti edilemez. Uygulama Instagram şifresi istemez ve giriş duvarlarını aşmaya çalışmaz. İçerikleri yalnızca indirme ve kullanma iznin olan hesaplarda kullan.

Uygulama yalnızca bilgisayarındaki `127.0.0.1` adresinde dinler.
