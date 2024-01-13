from flask import Flask, render_template,make_response
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/home')
class Home(Resource):
    # mimetype = "text/html"
    def get(self):
        return make_response(render_template('Home.html'))


if __name__ == '__main__':
    app.run(debug=True)