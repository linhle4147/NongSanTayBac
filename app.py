from flask import Flask, render_template # Nhớ thêm render_template ở đây

app = Flask(__name__)

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
"""
app = Flask(__name__)
app.secret_key = 'your_secret_key' # Thay bằng một chuỗi bất kỳ

# --- CẤU HÌNH GMAIL ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com' # Email của bạn
app.config['MAIL_PASSWORD'] = 'your-app-password'    # Mật khẩu ứng dụng (không phải mk chính)
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('contact.html') # File chứa code HTML của bạn

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # 1. Lấy dữ liệu từ Form
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        interest = request.form.get('interest')
        message_content = request.form.get('message')

        # 2. Tạo nội dung Email
        subject = f"Yêu cầu mới từ: {fullname}"
        body = f""
        Bạn có yêu cầu mới từ Form Website:
        
        - Họ tên: {fullname}
        - Email: {email}
        - Số điện thoại: {phone}
        - Lĩnh vực quan tâm: {interest}
        - Nội dung: {message_content}
        ""

        # 3. Gửi Email
        msg = Message(subject=subject,
                      recipients=['recipient-email@gmail.com'], # Email nhận thông báo
                      body=body)
        
        try:
            mail.send(msg)
            return "Cảm ơn bạn! Yêu cầu đã được gửi thành công."
        except Exception as e:
            return f"Có lỗi xảy ra: {str(e)}" 
"""
if __name__ == '__main__':
    app.run(debug=True)