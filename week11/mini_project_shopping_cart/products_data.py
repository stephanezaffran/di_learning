# Create a function named retrieve_all_products that should read all the products from the json file,
# and return it in a variable called all_products
# Create a second function named retrieve_requested_product that takes the product id of the selected product
# as a parameter (from the products template - see below).
# This function should read all the products from the json file, and return the product
# with the same id as the given parameter. Save the product in a variable called requested_product.

import json

def retrieve_all_products():
    with open("file.json", "r") as f:
        return json.load(f)

def retrieve_requested_product(product_id):
    all_products = retrieve_all_products()
    return all_products[product_id]


