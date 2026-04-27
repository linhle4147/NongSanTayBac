from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = 'nong_san_tay_nguyen_secret_key' # Cần thiết để dùng flash messages

# Cấu hình Email (Bạn cần thay thế MẬT KHẨU ỨNG DỤNG của mình vào đây)
EMAIL_SENDER = 'lebachlinh0347@gmail.com'
# https://myaccount.google.com/apppasswords
EMAIL_PASSWORD = 'uuxtflkqbktpmkzz' 
EMAIL_RECEIVER = 'lebachlinh0347@gmail.com'

@app.route('/')
def home():
    # Gọi file index.html trong thư mục templates
    return render_template('homePage.html')
@app.route('/about-us')
def about():
    return render_template('aboutUS.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/product')
def product():
    return render_template('product.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/news_detail')
def news_detail():
    return render_template('news_detail.html')

@app.route('/send_contact', methods=['POST'])
def send_contact():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    interest = request.form.get('interest')
    message = request.form.get('message')

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = f"Liên hệ mới từ Website: {fullname}"

    body = f"""
    Bạn nhận được một liên hệ mới từ Website Nông Sản:
    
    Họ và tên: {fullname}
    Email: {email}
    Số điện thoại: {phone}
    Lĩnh vực quan tâm: {interest}
    
    Nội dung tin nhắn:
    {message}
    """
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        # Sử dụng SMTP Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        flash('Yêu cầu của bạn đã được gửi thành công!', 'success')
    except Exception as e:
        print(f"Lỗi gửi email: {e}")
        flash('Có lỗi xảy ra khi gửi email. Hãy kiểm tra lại mật khẩu ứng dụng hoặc thử lại sau.', 'error')

    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)