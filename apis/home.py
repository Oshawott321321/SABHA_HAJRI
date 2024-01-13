from flask import make_response,render_template
from flask_restx import Namespace , Resource

api = Namespace('home')


@api.route('/home')
class Home(Resource):
    def get(self):
        return make_response(render_template('Home.html'))