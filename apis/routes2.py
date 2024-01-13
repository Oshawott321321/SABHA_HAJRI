from flask_restx import Namespace, Resource, fields

api = Namespace('route1', description='Cats related operations')

@api.route('/abcd')
class CatList(Resource):
    def get(self):
        return {}