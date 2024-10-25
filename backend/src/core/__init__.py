from os import environ
from flask import Flask
from src.core import db
from flask_session import Session
from flask_cors import CORS

def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    cors = CORS(app, supports_credentials=True)

    # Obtener la configuración del entorno
    env = environ.get("FLASK_ENV", env)  
    app.config.from_object(config[env])
    
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.config['SQLALCHEMY_ECHO'] = True
    
    Session(app)
    
    # Inicializar la base de datos
    try:
        db.init_app(app)
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")

    @app.cli.command(name="resetdb")
    def resetdb():
        """Reiniciar la base de datos."""
        db.reset_db()
    

    # from src.web.routes import register_routes
    # register_routes(app)

    return app

