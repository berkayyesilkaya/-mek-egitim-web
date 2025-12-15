# PythonAnywhere Deployment Rehberi

## Adımlar

### 1. Dosyaları Yükle
- PythonAnywhere Dashboard → Files
- Upload: app.py, requirements.txt, wsgi.py
- templates/ ve static/ klasörlerini yükle

### 2. Virtual Environment Oluştur
```bash
mkvirtualenv --python=/usr/bin/python3.10 kamu_web_env
pip install -r requirements.txt
```

### 3. Web App Yapılandır
- Dashboard → Web
- Add a new web app → Manual configuration → Python 3.10
- Source code: /home/KULLANICI/kamu_web
- WSGI file düzenle
- Virtual env: /home/KULLANICI/.virtualenvs/kamu_web_env

### 4. Static Files
- URL: /static/
- Directory: /home/KULLANICI/kamu_web/static/

### 5. Reload
- Yeşil "Reload" butonuna tıkla

## ADIM 6️⃣: GoDaddy Domain Bağlama

### ⚠️ ÖNEMLİ NOTLAR
- PythonAnywhere'de **özel domain kullanmak için PAID PLAN gerekir** (en ucuz: $5/ay)
- Free plan ile sadece `kullaniciadi.pythonanywhere.com` kullanabilirsiniz
- GoDaddy'den aldığınız domain'i bağlamak için upgrade yapmanız gerekecek

---

### ADIM 6.1: PythonAnywhere'de Domain Ekle

1. **PythonAnywhere Dashboard → "Web" sekmesi**

2. **"Add a new web app" yerine** aşağı kaydırın, **"Enter a new web address"** bölümünü bulun

3. Domain'inizi yazın:
   - `www.mekegittimdanismanlik.com` ← www'lu versiyonu yazın
   - Veya sadece: `mekegittimdanismanlik.com`

4. **"Add"** butonuna tıklayın

5. Karşınıza çıkan pencerede:
   - **"Use the same configuration as..."** seçeneğini seçin
   - Dropdown'dan mevcut web app'inizi seçin (örn: `mekkullaniciadi.pythonanywhere.com`)

6. **Create** butonuna tıklayın

✅ Şimdi web app listenizde 2 domain olmalı:
- ✓ `mekkullaniciadi.pythonanywhere.com`
- ✓ `www.mekegittimdanismanlik.com`

---

### ADIM 6.2: GoDaddy DNS Ayarlarını Yapın

Şimdi GoDaddy'ye gidip DNS kayıtlarını değiştireceğiz:

#### 1️⃣ GoDaddy'ye Giriş Yapın
- https://www.godaddy.com → Giriş
- **My Products** → Domain'inizi bulun
- Domain'in yanındaki **"DNS"** butonuna tıklayın

#### 2️⃣ Mevcut A Kayıtlarını Silin/Düzenleyin

**ÖNEMLİ:** Önce mevcut kayıtları not alın (yedek için)!

Şu kayıtları bulun ve **SİLİN**:
- Type: `A`, Name: `@` → SİL
- Type: `A`, Name: `www` → SİL (varsa)

#### 3️⃣ CNAME Kayıtları Ekleyin

**"Add" butonuna tıklayın** ve şu 2 kaydı ekleyin:

**KAYIT 1:**
```
Type: CNAME
Name: www
Value: webapp-XXXXX.pythonanywhere.com
TTL: 600 seconds (10 minutes)
```

**KAYIT 2:**
```
Type: CNAME
Name: @
Value: webapp-XXXXX.pythonanywhere.com
TTL: 600 seconds
```

⚠️ **`webapp-XXXXX` kısmını PythonAnywhere'den öğrenin:**
- PythonAnywhere → Web tab → Domain'iniz seçili
- "Configuration for www.mekegittimdanismanlik.com" başlığı altında
- **"CNAME target:"** yazan yerde göreceksiniz
- Örnek: `webapp-27182.pythonanywhere.com`

#### 4️⃣ Kaydet ve Bekle

- **"Save"** butonuna tıklayın
- DNS değişikliği **15 dakika - 48 saat** arasında yayılır
- Genellikle 30 dakika içinde çalışmaya başlar

---

### ADIM 6.3: SSL/HTTPS Sertifikası (ÜCRETSİZ)

Domain bağlandıktan sonra (24 saat içinde):

1. PythonAnywhere → **Web tab**

2. Aşağı kaydırın → **"Security"** bölümü

3. **"Force HTTPS"** seçeneğini aktifleştirin

4. **"Get certificate from Let's Encrypt"** butonuna tıklayın
   - ✅ Ücretsiz SSL sertifikası otomatik oluşturulacak

5. Sertifika oluşunca → **"Reload"** butonuna tıklayın

✅ Artık siteniz `https://www.mekegittimdanismanlik.com` üzerinden çalışacak!

---

### ADIM 6.4: Domain Yönlendirme (İsteğe Bağlı)

Eğer hem `www.mekegittimdanismanlik.com` hem de `mekegittimdanismanlik.com` çalışsın istiyorsanız:

**GoDaddy'de Forwarding Ekle:**

1. GoDaddy → My Products → Domain → **"Manage DNS"**

2. En altta **"Forwarding"** bölümü → **"Add Forwarding"**

3. Ayarlar:
   ```
   Forward from: mekegittimdanismanlik.com
   Forward to: https://www.mekegittimdanismanlik.com
   Forward type: 301 (Permanent)
   Forward settings: Forward only
   Update nameservers: No
   ```

4. **Save**

✅ Artık her iki adres de çalışacak!

---

## Test Checklist ✅

Domain bağlantısını test edin:

```bash
# 1. DNS propagation kontrolü
nslookup www.mekegittimdanismanlik.com

# 2. CNAME kaydı kontrolü  
dig www.mekegittimdanismanlik.com CNAME

# 3. Site erişimi
curl -I https://www.mekegittimdanismanlik.com
```

Veya online araçlar:
- https://dnschecker.org → Domain'inizi yazın
- https://www.whatsmydns.net → CNAME kayıtlarını kontrol edin

---

## Sorun Giderme 🔧

### ❌ "CNAME already exists"
- GoDaddy'de eski A kayıtlarını sildiğinizden emin olun
- Önce A kayıtlarını sil, sonra CNAME ekle

### ❌ "This site can't be reached"
- DNS propagation bekleniyor (24 saate kadar)
- `nslookup` ile DNS yayılımını kontrol edin

### ❌ "Not secure" / HTTP hatası
- SSL sertifikası henüz oluşmamış
- 24 saat bekleyin, sonra Let's Encrypt butonuna tekrar tıklayın

### ❌ Domain eklenemedi (PythonAnywhere)
- Paid plan'e upgrade etmelisiniz
- Account → Billing → Upgrade

---

## Özet - Yapılacaklar Listesi

- [ ] PythonAnywhere Paid Plan'e upgrade
- [ ] PythonAnywhere'de custom domain ekle
- [ ] `webapp-XXXXX` CNAME target'ı kopyala
- [ ] GoDaddy → DNS → Eski A kayıtlarını sil
- [ ] GoDaddy → 2 CNAME kaydı ekle (`www` ve `@`)
- [ ] 30-60 dakika bekle (DNS propagation)
- [ ] Domain'e giriş yap ve test et
- [ ] SSL sertifikası al (Let's Encrypt)
- [ ] Force HTTPS'i aktifleştir
- [ ] Domain forwarding ayarla (opsiyonel)

**Toplam Maliyet:** $5/ay (PythonAnywhere Hacker Plan)
