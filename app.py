from flask import Flask, render_template
from products import products
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', products=products)
@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)
if __name__ == '__main__':
    app.run(debug=True)
