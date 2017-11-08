import falcon
from birds.birds import Birds

api = application = falcon.API()

birds = Birds()
api.add_route('/birds', birds)
