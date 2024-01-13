from flask import Flask

from apis import all_routes

app = Flask(__name__)

all_routes.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
