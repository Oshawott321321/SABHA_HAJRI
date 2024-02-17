from flask_restx import Api

from .home    import api as route1
from .PersonRoutes import api as route2


all_routes = Api(doc="/tmp")

all_routes.add_namespace(route1,path='')
all_routes.add_namespace(route2,path='/data')