from flask import Flask, render_template
import json
import database_manager


app = Flask(__name__)
database_manager.create_database()

# @app.route('/realm/<realm>')
# def realm_index(realm):
#     return render_template('realm.html', realm=realm)
#
# @app.route('/particles')
# def particles_view():
#     with open('data.json','r') as f:
#         data = json.load(f)
#     return render_template('particles.html', particles=data)


@app.route("/")
@app.route("/products")
def products_page():

    data = database_manager.load_database()

    return """
        Currently, we don't have any product to sell, sorry!
    """


if __name__ == '__main__':
    app.run(debug=True)