# 🚀 DigitalOcean Deployment Rehberi - MEK Eğitim Danışmanlık

**Tam adım adım kurulum rehberi - Satın alma dahil!**

---

## 📋 İçindekiler

1. [Ön Hazırlık](#1-ön-hazırlık-5-dakika)
2. [GitHub'a Proje Yükleme](#2-githuba-proje-yükleme-10-dakika)
3. [DigitalOcean Hesap Açma](#3-digitalocean-hesap-açma-5-dakika)
4. [App Platform Kurulumu](#4-app-platform-kurulumu-15-dakika)
5. [GoDaddy Domain Bağlama](#5-godaddy-domain-bağlama-10-dakika)
6. [SSL Sertifikası](#6-ssl-sertifikası-otomatik)
7. [Test ve Yayınlama](#7-test-ve-yayınlama-5-dakika)

**Toplam Süre:** ~50 dakika  
**Toplam Maliyet:** $6/ay (ilk ay $0 - ücretsiz deneme)

---

## 📦 1. ÖN HAZIRLIK (5 dakika)

### ✅ Gerekli Şeyler:

- [x] Flask projesi hazır (✅ Sizde var!)
- [ ] GitHub hesabı (ücretsiz)
- [ ] DigitalOcean hesabı (ücretsiz açılacak)
- [ ] Kredi kartı/banka kartı (doğrulama için, ilk ay ücretsiz)
- [ ] GoDaddy domain erişimi

### ✅ Proje Dosyaları Kontrol:

```bash
kamu_web 3/
├── app.py                 ✅ Var
├── wsgi.py                ✅ Var
├── requirements.txt       ✅ Var (gunicorn eklendi)
├── runtime.txt            ✅ Var (Python 3.10)
├── .gitignore            ✅ Var (Git için)
├── templates/            ✅ Var
│   ├── index.html
│   ├── blog.html
│   ├── hakkimizda.html
│   └── hizmetlerimiz.html
└── static/               ✅ Var
    ├── style.css
    ├── images/
    └── videos/
```

**Herşey hazır!** ✅

---

## 📤 2. GITHUB'A PROJE YÜKLEME (10 dakika)

### Adım 2.1: GitHub Hesabı Açın (varsa geçin)

1. **https://github.com** → "Sign up" tıklayın
2. Email, kullanıcı adı, şifre girin
3. Email doğrulama yapın

### Adım 2.2: Yeni Repository Oluşturun

1. GitHub'da sağ üst köşe → **"+"** → **"New repository"**

2. Şu bilgileri girin:
   ```
   Repository name: mek-egitim-web
   Description: MEK Eğitim Danışmanlık Web Sitesi
   Privacy: Public (ücretsiz) veya Private (paralı)
   ❌ Initialize this repository... → TIKLAMAYIN!
   ```

3. **"Create repository"** yeşil butona tıklayın

### Adım 2.3: Projeyi GitHub'a Yükleyin

**Terminal açın** (Cursor içinde veya sistem terminalinde):

```bash
# 1. Proje klasörüne gidin
cd "/Users/berkayyesilkaya/Desktop/kamu_web 3"

# 2. Git başlatın
git init

# 3. Dosyaları ekleyin
git add .

# 4. İlk commit
git commit -m "Initial commit - MEK Eğitim Danışmanlık web sitesi"

# 5. GitHub'a bağlayın (aşağıdaki KULLANICI_ADINIZ kısmını değiştirin!)
git remote add origin https://github.com/KULLANICI_ADINIZ/mek-egitim-web.git

# 6. Main branch oluşturun
git branch -M main

# 7. GitHub'a yükleyin
git push -u origin main
```

**Not:** GitHub kullanıcı adı/şifre sorarsa:
- Username: GitHub kullanıcı adınız
- Password: **Personal Access Token** (şifre değil!)
  - GitHub → Settings → Developer settings → Personal access tokens → Generate new token
  - `repo` yetkisi verin
  - Oluşan token'ı kopyalayın ve şifre yerine yapıştırın

### Adım 2.4: Kontrol Edin

GitHub'da repository sayfanıza gidin → Tüm dosyaları görmeli:

```
✅ app.py
✅ requirements.txt
✅ runtime.txt
✅ templates/
✅ static/
✅ .gitignore
```

**GitHub kısmı tamamlandı!** ✅

---

## 💳 3. DIGITALOCEAN HESAP AÇMA (5 dakika)

### Adım 3.1: DigitalOcean'a Kaydolun

1. **https://www.digitalocean.com** → "Sign Up" tıklayın

2. Kayıt seçenekleri:
   - **GitHub ile giriş** (önerilen, daha hızlı) ✅
   - Veya Email ile kayıt

3. **GitHub ile devam ederseniz:**
   - "Sign up with GitHub" → GitHub'a yönlendirir
   - "Authorize DigitalOcean" → Yetki verin
   - Otomatik geri döner

### Adım 3.2: Email Doğrulama

- Email'inize gelen linke tıklayın
- "Verify your email" → Doğrulama tamamlanır

### Adım 3.3: Ödeme Bilgilerini Ekleyin

**Önemli Not:** 
- İlk kayıtta $200 ücretsiz kredi verilebilir (promosyon varsa)
- İlk 60 gün ücretsiz deneme
- Kart doğrulama için $1 çekilir, hemen iade edilir

**Adımlar:**

1. Dashboard → "Billing" sekmesi

2. "Add Payment Method" tıklayın

3. Kart bilgilerini girin:
   ```
   Kart numarası: ____
   Son kullanma: __/__
   CVV: ___
   Kart sahibi: ____
   ```

4. **"Add Payment Method"** → Kaydet

5. Doğrulama:
   - Kartınızdan $1 çekilir (test)
   - Hemen iade edilir
   - Kart onaylanır ✅

### Adım 3.4: Promo Kodu (Varsa)

**Öğrenci misiniz?**
- GitHub Student Developer Pack → $200 ücretsiz DigitalOcean kredisi
- https://education.github.com/pack

**Genel Promo:**
- İlk kayıt bonusu genellikle otomatik eklenir
- Billing sayfasında "Credits" bölümünde görünür

**DigitalOcean hesabınız hazır!** ✅

---

## 🚀 4. APP PLATFORM KURULUMU (15 dakika)

### Adım 4.1: App Platform'a Gidin

1. DigitalOcean Dashboard → Sol menü → **"Apps"** tıklayın

2. Mavi **"Create App"** butona tıklayın

### Adım 4.2: Kaynak Seçimi (Source)

**"Service Provider" seçimi:**

1. **GitHub** seçin

2. "Authorize DigitalOcean" → GitHub penceresi açılır

3. GitHub'da:
   - "Authorize digitalocean" yeşil butona tıklayın
   - Şifrenizi onaylayın

4. Repository listesi gelecek:
   - **"mek-egitim-web"** repository'nizi seçin
   - Branch: **"main"** seçin
   - "Autodeploy" → **Açık bırakın** ✅ (Git'e push yapınca otomatik deploy olur)

5. **"Next"** mavi buton → İleri

### Adım 4.3: Resources (Kaynak Ayarları)

**Otomatik algılama:**

DigitalOcean Flask uygulamanızı algılayacak:

```
✅ Type: Web Service
✅ Name: mek-egitim-web
✅ Source Directory: /
✅ Detected: Python (Flask)
```

**Düzenleme yapın:**

1. Kaynak adına tıklayın → "Edit" buton

2. **Build Command** kutusuna:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Command** kutusuna:
   ```bash
   gunicorn --worker-tmp-dir /dev/shm app:app
   ```

4. **HTTP Port:** `8080` (otomatik)

5. **HTTP Request Routes:** `/` (otomatik)

6. **"Back"** ile geri dönün

7. **"Next"** → İleri

### Adım 4.4: Environment Variables (Çevre Değişkenleri)

**Email ayarlarını ekleyin:**

1. "Add Environment Variable" → "Bulk Editor" tıklayın

2. Şu değişkenleri ekleyin:
   ```env
   MAIL_USERNAME=info@mekegitimdanismanlik.com
   MAIL_PASSWORD=your-gmail-app-password
   SECRET_KEY=mek-egitim-gizli-anahtar-2024-digitalocean
   ```

   **NOT:** 
   - `MAIL_USERNAME`: Gmail adresiniz
   - `MAIL_PASSWORD`: Gmail App Password (Gmail → Security → 2FA → App passwords)
   - `SECRET_KEY`: Güvenlik anahtarı (değiştirebilirsiniz)

3. **"Encrypt"** seçeneğini açın (şifre için) 🔒

4. **"Save"** → Kaydet

5. **"Next"** → İleri

### Adım 4.5: App Info (Uygulama Bilgileri)

1. **App Name:** `mek-egitim-web`

2. **Region:** 
   - **Frankfurt (fra1)** seçin ✅ (Türkiye'ye en yakın!)
   - Veya Amsterdam (ams3)

3. **"Next"** → İleri

### Adım 4.6: Plan Seçimi (ÖNEMLI! 💰)

**Pricing Plan seçimi:**

```
Basic Plan:
├─ $5/month (512MB RAM, 1 vCPU) ← BUNU SEÇİN ✅
├─ $12/month (1GB RAM)
└─ $25/month (2GB RAM)
```

**Seçim:**

1. **"Basic"** tab'ını seçin

2. **"$5/mo"** plan seçin:
   ```
   ✅ 512MB RAM / 1 vCPU
   ✅ 1TB bandwidth
   ✅ Always On (hiç uyumaz)
   ✅ Free SSL
   ✅ Automatic deployments
   ```

3. **"Launch Basic App"** mavi buton → Başlat!

### Adım 4.7: Deploy Süreci (Otomatik)

**Şimdi DigitalOcean sizin için:**

```
1. ⏳ Building... (2-3 dakika)
   ├─ GitHub'dan kodu çekiyor
   ├─ requirements.txt yükleniyor
   ├─ Python environment hazırlanıyor
   └─ Gunicorn yapılandırılıyor

2. ⏳ Deploying... (1-2 dakika)
   ├─ Container oluşturuluyor
   ├─ App başlatılıyor
   └─ Health check yapılıyor

3. ✅ Live! (Deploy tamamlandı)
   └─ Site yayında!
```

**Bekleyin:** ~3-5 dakika

### Adım 4.8: İlk Test

Deploy tamamlanınca:

1. **Yeşil "Live"** yazısını göreceksiniz ✅

2. **URL görünecek:** `mek-egitim-web-xxxxx.ondigitalocean.app`

3. URL'ye tıklayın → **SİTENİZ AÇILIYOR!** 🎉

**Tebrikler! DigitalOcean'da yayındasınız!** ✅

---

## 🌐 5. GODADDY DOMAIN BAĞLAMA (10 dakika)

### Adım 5.1: DigitalOcean'da Domain Ekle

1. DigitalOcean Dashboard → **Apps** → Uygulamanızı seçin

2. **"Settings"** tab → **"Domains"** bölümü

3. **"Add Domain"** butonuna tıklayın

4. Domain'inizi yazın:
   ```
   www.mekegittimdanismanlik.com
   ```

5. **"Add Domain"** → Ekle

6. ⚠️ **Şu bilgileri NOT ALIN:**
   ```
   CNAME Record:
   Name: www
   Value: mek-egitim-web-xxxxx.ondigitalocean.app
   ```

### Adım 5.2: GoDaddy DNS Ayarları

**GoDaddy'ye gidin:**

1. **https://www.godaddy.com** → Giriş yapın

2. **"My Products"** → Domain'inizi bulun

3. Domain yanında **"DNS"** butona tıklayın

### Adım 5.3: Mevcut Kayıtları Temizleyin

**ÖNEMLİ:** Önce yedek alın! Kayıtları bir yere not edin.

**Şu kayıtları SİLİN:**

- Type: `A`, Name: `@` → **Sil (kalem ikonu → Delete)**
- Type: `A`, Name: `www` → **Sil** (varsa)

### Adım 5.4: CNAME Kayıtları Ekleyin

**KAYIT 1 - www:**

1. **"Add"** butona tıklayın

2. Bilgileri girin:
   ```
   Type: CNAME
   Name: www
   Value: mek-egitim-web-xxxxx.ondigitalocean.app
   TTL: 600 seconds (10 minutes)
   ```

3. **"Save"** → Kaydet

**KAYIT 2 - root (@):**

1. Tekrar **"Add"** tıklayın

2. Bilgileri girin:
   ```
   Type: CNAME
   Name: @
   Value: mek-egitim-web-xxxxx.ondigitalocean.app
   TTL: 600 seconds
   ```

3. **"Save"** → Kaydet

**⚠️ UYARI:** Bazı GoDaddy paketleri root (@) için CNAME izin vermez. O zaman:

**Alternatif - A Record kullanın:**

1. DigitalOcean'da App'inizin IP adresini alın:
   - Settings → Domains → "View Records"
   - IP adresini not edin

2. GoDaddy'de:
   ```
   Type: A
   Name: @
   Value: IP_ADRESI (DigitalOcean'dan aldığınız)
   TTL: 600 seconds
   ```

### Adım 5.5: DNS Propagation (Yayılma)

**Bekleyin:** 15-60 dakika

**Kontrol edin:**

```bash
# Terminal'de:
nslookup www.mekegittimdanismanlik.com

# Veya online:
https://dnschecker.org
```

**Yeşil ✅ görünce hazır!**

---

## 🔒 6. SSL SERTİFİKASI (Otomatik)

### Adım 6.1: DigitalOcean Otomatik SSL

**DigitalOcean otomatik Let's Encrypt sertifikası ekler!**

1. Domain DNS'i yayıldıktan sonra (30-60 dakika)

2. DigitalOcean → Apps → Uygulamanız → **"Settings"** → **"Domains"**

3. Domain'inizin yanında:
   ```
   ⏳ Pending → Sertifika bekleniyor
   ✅ Active → SSL aktif!
   ```

**Otomatik olur, bir şey yapmanıza gerek yok!**

### Adım 6.2: HTTPS Yönlendirme

DigitalOcean otomatik HTTP → HTTPS yönlendirmesi yapar ✅

**Test edin:**
- http://www.mekegittimdanismanlik.com → Otomatik https:// olur
- Tarayıcıda kilit 🔒 simgesi görünür

---

## ✅ 7. TEST VE YAYINLAMA (5 dakika)

### Test Checklist:

```bash
✅ https://www.mekegittimdanismanlik.com → Açılıyor
✅ Ana sayfa → Görseller yükleniyor
✅ Hakkımızda → Sayfa çalışıyor
✅ Hizmetlerimiz → Sayfa çalışıyor
✅ Blog → Sayfa çalışıyor
✅ İletişim formu → Form gönderiliyor
✅ Responsive → Mobilde güzel görünüyor
✅ SSL → Yeşil kilit var
✅ Hız → Sayfalar hızlı yükleniyor
```

### Adım 7.1: İletişim Formu Testi

1. Sitenizde iletişim formunu doldurun

2. "Gönder" → Flash mesaj görünmeli

3. DigitalOcean Dashboard → Apps → **"Runtime Logs"**
   - Console'da formun geldiğini görmeli

4. Email gelmiyor mu?
   - Gmail App Password doğru mu kontrol edin
   - Environment variables doğru mu?

### Adım 7.2: Hız Testi

**Online araçlar:**

- https://pagespeed.web.dev → URL'nizi test edin
- https://gtmetrix.com → Performans analizi

**Hedef:**
- ✅ 1-2 saniye load time
- ✅ 90+ performance score

### Adım 7.3: Mobil Test

**Telefonda test edin:**

1. www.mekegittimdanismanlik.com → Aç

2. Tüm sayfaları kontrol et

3. İletişim formu → Mobilde de çalışmalı

---

## 🎉 TAMAMLANDI!

### ✅ Başarıyla Yayınlandınız!

```
🌐 Web Site: https://www.mekegittimdanismanlik.com
🔒 SSL: Aktif (Let's Encrypt)
⚡ Hız: Frankfurt sunucuları (hızlı)
💰 Maliyet: $6/ay (ilk ay ücretsiz)
📈 Kapasite: 3,000 ziyaretçi/gün
🚀 Deploy: Git push ile otomatik
```

---

## 🔄 GÜNCELLEMELER (Gelecekte)

### Kod Değişikliği Yaptığınızda:

```bash
# 1. Dosyaları düzenleyin
# 2. Git'e ekleyin
git add .
git commit -m "Güncelleme açıklaması"
git push origin main

# 3. DigitalOcean otomatik deploy eder! (2-3 dakika)
```

**Otomatik deployment aktif! ✅**

---

## 💰 MALIYET ANALİZİ

### Aylık Maliyet:

```
DigitalOcean App Platform: $6/ay
├─ 512MB RAM
├─ 1 vCPU
├─ 1TB bandwidth
├─ Always On
├─ Free SSL
└─ Otomatik backups

GoDaddy Domain: $15/yıl = ~$1.25/ay
├─ Domain
└─ DNS yönetimi

TOPLAM: ~$7.25/ay ($87/yıl)
```

### İlk Ay (Deneme):

```
DigitalOcean: $0 (60 gün ücretsiz veya $200 kredi)
GoDaddy: $0 (zaten ödendi)

TOPLAM: $0 ✅
```

---

## 🆘 SORUN GİDERME

### ❌ "Application failed to respond"

**Çözüm:**

1. DigitalOcean → Apps → **"Runtime Logs"**
2. Hata mesajını okuyun
3. Genellikle:
   - requirements.txt eksik paket
   - Environment variable yanlış

### ❌ "Domain not resolving"

**Çözüm:**

1. DNS propagation bekleyin (60 dakikaya kadar)
2. GoDaddy DNS kayıtlarını kontrol edin
3. `nslookup www.mekegittimdanismanlik.com` → Test edin

### ❌ "SSL Certificate Pending"

**Çözüm:**

1. DNS tamamen yayılmış mı? (dnschecker.org)
2. 24 saat bekleyin
3. DigitalOcean Support'a ticket açın (hızlı cevap verirler)

### ❌ "İletişim formu çalışmıyor"

**Çözüm:**

1. Gmail App Password doğru mu?
2. Environment variables doğru yazıldı mı?
3. `app.py` içinde `mail.send()` satırları aktif mi?

---

## 📞 DESTEK

**DigitalOcean Support:**
- Dashboard → "?" ikonu → "Contact Support"
- Genellikle 1-2 saat içinde cevap verirler
- Community forumlar aktif

**Bu Rehber:**
- Takıldığınız yerden devam edebilirsiniz
- Her adım detaylı açıklanmış

---

## 🎓 SONRAKI ADIMLAR (Opsiyonel)

### 1. Google Analytics Ekle
- Ziyaretçi istatistikleri
- Trafik analizi

### 2. Email Marketing
- Newsletter formu
- Mailchimp entegrasyonu

### 3. Blog Dinamik Yap
- Database ekle (PostgreSQL)
- Admin paneli

### 4. SEO Optimizasyonu
- Meta tags
- Sitemap.xml
- robots.txt

---

## ✅ TAMAMLANDI! 🎉

**Artık profesyonel bir web siteniz var!**

- ⚡ Hızlı (Frankfurt sunucuları)
- 🔒 Güvenli (SSL)
- 🌍 Global erişim
- 💰 Ekonomik ($6/ay)
- 🚀 Otomatik güncellemeler

**Başarılar dileriz! 🎓**

---

*Bu rehber MEK Eğitim Danışmanlık için özel hazırlanmıştır.*
*Son güncelleme: Aralık 2024*

