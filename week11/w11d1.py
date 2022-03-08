
import Flask

app = flask.Flask(__name__)

users = ["bob","dan"]

@app.route('/<blog>')
def index(username):
    html = '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, {}!</h1>
    </body>
</html>'''.format(map(lambda x: x, users))

    return html


if __name__ == "__main__":
    app.run()