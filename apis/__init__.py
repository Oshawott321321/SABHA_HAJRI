from flask_restx import Api

from .home    import api as route1
from .routes2 import api as route2


all_routes = Api()

all_routes.add_namespace(route1)
all_routes.add_namespace(route2)