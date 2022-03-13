

import products_data
from flask import Flask, render_template, render_template_string
import json


app = Flask(__name__, template_folder='template')


# In this file, we will be using the functions written in the products_data.py. How can we access these?
# Create a route with the following URL /, that will trigger a function that returns the a template that welcomes the user,
# and tells them about your store.
# Create a route with the following URL /products, that will trigger a function that returns a template that displays
# all the products. Each product should have
# a button that directs the user to the /products/<product_id> URL.
# Create a route with the following URL /products/<product_id>, that will trigger a function that returns a template
# that displays the requested product. The product should have a button that allows the user to add this product to his cart.


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/products/')
def product():

    return render_template("products.html", product="product")


# @app.route('/cart/')
# def cart():
#     with open('data.json','r') as f:
#         data = json.load(f)
#     return render_template('particles.html', particles = data)

if __name__ == '__main__':
    app.run(debug=True)


# Part II
# At this point, we will be creating the functionality that allows the user to add and delete products from their cart.
#
# In the my_app.py file
# Create a route with the following URL /cart that leads to the cart template (it should display all the products in
# the cart with their price, the total price and a button next to each product that allows the user to delete it from his cart)
# Create a variable named cart_item. This variable will hold all the products added to the cart.
# Create a route with the following URL /add_product_to_cart/<product_id> that triggers a function.
# This function should take the product id as a parameter, and append the product details to the cart_item variable.
# Create a route with the following URL /delete_product_from_cart/<product_id> that triggers a function.
# This function should take the product id as a parameter, and delete the product details from the cart_item variable.
# Note : If you feel comfortable with json, you could write the products into a cart.json file




