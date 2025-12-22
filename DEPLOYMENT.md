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

## Domain Bağlama
- Paid plan gerekir ($5/ay)
- Web tab → Add custom domain → mekegittimdanismanlik.com
