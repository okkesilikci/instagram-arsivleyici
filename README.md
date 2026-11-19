# IG Arşivleyici – Chrome eklentisi (ilk prototip)

## Kurulum
1. GitHub deposunu ZIP olarak indir ve aç.
2. Chrome'da `chrome://extensions` adresini aç.
3. Sağ üstten **Geliştirici modu**nu aç.
4. **Paketlenmemiş öğe yükle** seçeneğine bas.
5. İndirdiğin proje klasörünün içindeki `chrome-extension` klasörünü seç.
6. Chrome'da Instagram'da açık profil sayfasına git, eklenti simgesine bas ve **Profili tara** düğmesini kullan.

## İlk sürümün sınırları
- Yalnızca Instagram sayfasında tarayıcıya yüklenen profil ızgarası görsellerini toplar.
- Carousel gönderilerinde ilk aşamada ızgaradaki kapak görselini alır.
- Profil ızgarasında gerçek tarih bilgisi DOM'da sunulmuyorsa dosya adı `tarih-yok_NNN` olur; doğru yayın tarihi garantisi yoktur.
- Instagram arayüzü değişirse seçicilerin güncellenmesi gerekebilir.
- Instagram'ın erişim, hız ve içerik gösterim sınırlarını aşmaz.
- Eklenti şifre, çerez veya oturum bilgisi toplamaz.

Bu prototipin amacı, Chrome'da oturum açılmış ve kullanıcı tarafından görüntülenebilen profil görsellerini toplama akışını test etmektir.
