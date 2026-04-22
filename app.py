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
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)