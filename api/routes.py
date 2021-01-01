from flask_restful import Api, Resource
#from especies import routes as especies_routes
from flask import Blueprint

def initialize_routes(app):
    """
    Inicializa rotas gerais

    Parameters:
        app (class): instância de app
        api (class): instância de api
    """
    api = Api(app)
    
    modules = [
        #especies_routes,
    ]
    
    # itera módulos e inicializa rotas
    api.add_resource(IndexPage, '/')
    
    for module in modules:
        module.initialize_routes(app, api)

class IndexPage(Resource):
    def get(self):
        return "API BD Agroflorestas!"
