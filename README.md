# Instagram Arşivleyici

Instagram fotoğraflarını kronolojik olarak düzenlemek ve seçilenleri ZIP olarak indirmek için tarayıcı tabanlı bir araç.

## İlk sürüm

- Birden fazla fotoğrafı bilgisayardan içe aktarma
- Fotoğrafları paylaşım tarihine göre sıralama
- Tek tek veya toplu seçim
- Dosya adlandırma: `AA_YYYY_NNN.ext` (ör. `11_2026_001.jpg`)
- Seçilen fotoğrafları tek ZIP dosyasında indirme
- Görseller tarayıcıda işlenir; uygulamaya yüklenmez

## Çalıştırma

`index.html` dosyasını tarayıcıda açman yeterli. ZIP oluşturma için JSZip CDN üzerinden yüklenir; internet bağlantısı gerekir.

## Instagram erişimi hakkında

Profil URL alanı bu ilk prototipte yalnızca arşiv etiketi olarak tutulur; Instagram'dan otomatik gönderi çekmez. Instagram, üçüncü taraf uygulamalara herkese açık herhangi bir profilin tüm gönderilerini topluca listeleyip indirmek için garantili genel bir API sunmaz. Giriş duvarlarını, erişim kontrollerini veya hız sınırlarını aşan yöntemler kullanılmaz.

Otomatik içe aktarma daha sonra yalnızca platformun izin verdiği bir API/entegrasyon veya kullanıcının yetkili olarak dışa aktardığı içerik üzerinden eklenebilir.

## Kullanım

1. `index.html` dosyasını aç.
2. Fotoğrafları seç.
3. Her fotoğrafın paylaşım tarihini gir.
4. İstediğin fotoğrafları seç ve ZIP indir.

Dosyalar tarih sırasına göre adlandırılır. Aynı ay içindeki sıra numaraları kronolojik sıraya göre verilir.
