from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Mail ayarları (Gmail örneği)
app.config['SECRET_KEY'] = 'mek-egitim-gizli-anahtar-2024'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') or 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') or 'your-app-password'
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME') or 'your-email@gmail.com'

mail = Mail(app)

# Anasayfa
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

# Hakkımızda
@app.route('/hakkimizda')
@app.route('/hakkimizda.html')
def about():
    return render_template('hakkimizda.html')

# Hizmetlerimiz
@app.route('/hizmetlerimiz')
@app.route('/hizmetlerimiz.html')
def services():
    return render_template('hizmetlerimiz.html')

# Blog Rotası
@app.route('/blog')
@app.route('/blog.html')
def blog():
    return render_template('blog.html')

# İletişim Formu
@app.route('/iletisim-gonder', methods=['POST'])
def send_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_body = request.form.get('message')
        
        # Konsola yazdır (debug için)
        print(f"\n{'='*50}")
        print(f"YENİ İLETİŞİM FORMU (MEK)")
        print(f"{'='*50}")
        print(f"Ad Soyad: {name}")
        print(f"E-posta: {email}")
        print(f"Mesaj: {message_body}")
        print(f"{'='*50}\n")
        
        try:
            # 1. Bize Gelen Mail (YENİ MAİL ADRESİ)
            msg = Message(f"MEK | Yeni İletişim Formu: {name}",
                          sender=app.config['MAIL_DEFAULT_SENDER'],
                          recipients=['info@mekegitimdanismanlik.com']) 
            
            msg.body = f"""
Ad Soyad: {name}
E-posta: {email}
Mesaj:
{message_body}
"""
            # mail.send(msg) # Gerçek e-posta gönderme hattı
            
            # 2. Kullanıcıya Giden Teşekkür Maili (GÜNCEL BİLGİLERLE)
            thank_you_msg = Message("MEK | Mesajınız Ulaştı!",
                                    sender=app.config['MAIL_DEFAULT_SENDER'],
                                    recipients=[email])
            thank_you_msg.html = (
                f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Mesajınız Ulaştı</title>
    <style>
        body {{ font-family: 'Poppins', sans-serif; background-color: #f4f7f6; margin: 0; padding: 0; }}
        .email-container {{ max-width: 600px; margin: 40px auto; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); overflow: hidden; border-top: 5px solid #001F3F; }}
        .header {{ background-color: #001F3F; color: #ffffff; padding: 25px; text-align: center; }}
        .logo {{ font-size: 28px; font-weight: 700; margin: 0; }}
        .content {{ padding: 30px; line-height: 1.6; color: #333; }}
        .message {{ margin-bottom: 25px; border-left: 4px solid #b30000; padding-left: 15px; background-color: #fffafa; }}
        .message p {{ margin: 5px 0; }}
        .contact-info {{ margin-top: 25px; padding: 15px; border-top: 1px solid #eee; font-size: 14px; color: #666; }}
        .contact-item {{ margin-bottom: 5px; }}
        .footer {{ padding: 20px; text-align: center; font-size: 12px; color: #999; background-color: #f0f0f0; }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <div class="logo">MEK</div>
            <p style="margin: 0; opacity: 0.9;">Eğitim Danışmanlık</p>
        </div>
        <div class="content">
            <h2 style="color: #667eea;">Sayın {name},</h2>
            <div class="message">
                <p>Bize ulaştığınız için çok teşekkür ederiz! 🎓</p>
                <p>Mesajınızı aldık ve en kısa sürede size geri dönüş yapacağız.</p>
            </div>
            <p>Eğitim yolculuğunuzda size yardımcı olmaktan mutluluk duyarız.</p>
            <div class="contact-info">
                <p><strong>İletişim Bilgilerimiz:</strong></p>
                <div class="contact-item">📞 +90 533 420 2195</div>
                <div class="contact-item">📧 info@mekegitimdanismanlik.com</div>
                <div class="contact-item">📍 İstanbul</div>
            </div>
        </div>
        <div class="footer">
            <p>© 2024 MEK Eğitim Danışmanlık. Tüm hakları saklıdır.</p>
        </div>
    </div>
</body>
</html>
                """
            )
            # mail.send(thank_you_msg) 
            
            flash('Mesajınız başarıyla gönderildi! En kısa sürede size dönüş yapacağız.', 'success')
        except Exception as e:
            print(f"Mail gönderme hatası: {str(e)}")
            flash('Mesajınız başarıyla gönderildi, ancak sistemimizde bir mail gönderme hatası oluştu. Lütfen merak etmeyin, size en kısa sürede geri dönüş yapacağız!', 'warning')

        return redirect(url_for('home') + '#iletisim')

if __name__ == '__main__':
    app.run(debug=True)