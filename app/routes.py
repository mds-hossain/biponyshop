from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/product')
def product():
    return render_template('product.html')

@main.route('/cart')
def cart():
    return render_template('cart.html')
