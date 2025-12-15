# KAMU Eğitim Danışmanlık Web Sitesi

Flask tabanlı dinamik eğitim danışmanlık web sitesi.

## Özellikler

✅ **Responsive tasarım** - Mobil, tablet ve masaüstü uyumlu  
✅ **Flask backend** - Python ile güçlendirilmiş  
✅ **HTML email gönderme** - Profesyonel tasarımlı mail içeriği  
✅ **İletişim formu** - Otomatik mail bildirimleri  
✅ **Modern UI** - Gradient renkler ve animasyonlar  

## Kurulum

### 1. Gerekli paketleri yükleyin

```bash
pip3 install flask flask-mail
```

### 2. Uygulamayı çalıştırın

```bash
python3 app.py
```

Tarayıcınızda `http://127.0.0.1:5000` adresini açın.

## Mail Yapılandırması

İletişim formundan gelen maillerin çalışması için aşağıdaki adımları izleyin:

### Gmail ile Mail Gönderimi (Önerilen)

1. **Gmail hesabınızda 2 faktörlü doğrulamayı açın**
   - Google Hesabım → Güvenlik → 2 Adımlı Doğrulama

2. **Uygulama şifresi oluşturun**
   - Google Hesabım → Güvenlik → Uygulama şifreleri
   - "Posta" ve cihaz seçin
   - Oluşturulan 16 haneli şifreyi kopyalayın

3. **Ortam değişkenlerini ayarlayın**

   **macOS/Linux:**
   ```bash
   export MAIL_USERNAME="your-email@gmail.com"
   export MAIL_PASSWORD="your-16-digit-app-password"
   ```

   **Windows (CMD):**
   ```cmd
   set MAIL_USERNAME=your-email@gmail.com
   set MAIL_PASSWORD=your-16-digit-app-password
   ```

4. **Kalıcı yapmak için (macOS/Linux):**
   
   `~/.zshrc` veya `~/.bashrc` dosyanıza ekleyin:
   ```bash
   export MAIL_USERNAME="your-email@gmail.com"
   export MAIL_PASSWORD="your-16-digit-app-password"
   ```
   
   Sonra:
   ```bash
   source ~/.zshrc  # veya source ~/.bashrc
   ```

### Alternatif: Doğrudan Kodda Değiştirme

Eğer ortam değişkenleri kullanmak istemiyorsanız, `app.py` dosyasında:

```python
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'
```

⚠️ **GÜVENLİK UYARISI:** Gerçek şifrenizi asla kodda saklamayın! Sadece test için kullanın.

## Mail Özellikleri

### Gönderilen Mailler

1. **Yöneticiye Mail** - Form gönderildiğinde `info@kamu.com` adresine gelir
   - HTML formatında profesyonel tasarım
   - Gönderen bilgileri ve mesaj içeriği
   - Kolay okunabilir gradient header

2. **Kullanıcıya Teşekkür Maili** - Form gönderen kişiye otomatik teşekkür
   - Markalı KAMU tasarımı
   - İletişim bilgileri
   - Profesyonel sunum

### Mail Şablonu Özellikleri

- 📱 Responsive HTML email tasarımı
- 🎨 Gradient renkler ve modern görünüm
- ✨ Emoji kullanımı ile görsel zenginlik
- 📊 Düzenli ve okunabilir içerik yapısı

## Test Etme

Mail sistemi çalışmasa bile form verisi konsola yazdırılır:

```bash
==================================================
YENİ İLETİŞİM FORMU
==================================================
Ad Soyad: Test Kullanıcı
E-posta: test@example.com
Mesaj: Test mesajı
==================================================
```

## Dosya Yapısı

```
kamu_web/
│
├── app.py                 # Flask uygulaması ve mail sistemi
├── requirements.txt       # Python bağımlılıkları
├── README.md             # Bu dosya
│
├── static/
│   ├── style.css         # CSS stilleri + flash mesaj stilleri
│   ├── images/           # Resim dosyaları
│   └── videos/           # Video dosyaları (varsa)
│
└── templates/
    ├── index.html        # Anasayfa + flash mesaj desteği
    ├── hakkimizda.html   # Hakkımızda sayfası
    └── hizmetlerimiz.html # Hizmetler sayfası
```

## Özelleştirme

### Mail Alıcı Adresini Değiştirme

`app.py` dosyasında:

```python
recipients=['info@kamu.com']  # Buraya kendi mail adresinizi yazın
```

### Mail Tasarımını Değiştirme

`app.py` dosyasındaki `html` parametresindeki HTML kodunu düzenleyin. Inline CSS kullanımına dikkat edin (çoğu email istemcisi external CSS'i desteklemez).

## Sorun Giderme

### Mail Gönderilmiyor

1. **Ortam değişkenlerini kontrol edin:**
   ```bash
   echo $MAIL_USERNAME
   echo $MAIL_PASSWORD
   ```

2. **Gmail uygulama şifresi kullandığınızdan emin olun** (normal şifre değil)

3. **Konsol çıktısına bakın** - Hata mesajları orada görünecektir

4. **Gmail'de "Güvenli olmayan uygulamalara izin ver" ayarını kontrol edin** (eski hesaplarda)

### Flash Mesajları Görünmüyor

Flash mesajları sadece `index.html` sayfasında görünür. Diğer sayfalarda da göstermek isterseniz aynı flash mesaj kodunu diğer HTML dosyalarına da ekleyin.

## Geliştirme Modunda Çalıştırma

Debug modu varsayılan olarak açık:

```python
app.run(debug=True)
```

Production ortamında `debug=False` yapın ve WSGI server kullanın (Gunicorn, uWSGI vb.)

## Lisans

© 2024 KAMU Eğitim Danışmanlık. Tüm hakları saklıdır.

## İletişim

- 📧 E-posta: info@kamu.com
- 📞 Telefon: +90 532 392 6174
- 📍 Adres: Beşiktaş, İstanbul
