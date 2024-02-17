from flask import make_response,render_template,redirect,url_for
from flask_restx import Namespace , Resource

api = Namespace('home')


@api.route('/home')
class Home(Resource):
    def get(self):
        return make_response(render_template('Home.html'))

@api.route("/")
class actualHome(Resource):
    def get(self):
        return redirect(url_for('Data_form'))