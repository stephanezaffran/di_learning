from flask import Flask, render_template
import faker
import json

app = Flask(__name__, template_folder="./templates")



@app.route('/')
def show():

    return render_template('index.html', title="my title", text="hello to my first app")


if __name__ == '__main__':
    app.run(debug=True)