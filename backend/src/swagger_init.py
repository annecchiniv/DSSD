from flasgger import Swagger

def initialize_swagger(app):

    app.config['SWAGGER'] = {
        "title": "API de documentación",
        "uiversion": 3,
        "description": "Documentación de la API",
        "version": "1.0.0",
        "specs_route": "/docs_api",
        "swagger_ui": True,   
        "termsOfService": None,
        "hide_top_bar": True
        
    }

    Swagger(app)
