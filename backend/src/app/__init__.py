from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from src.core.models import db
from src.config.config import Config
from flask_jwt_extended import JWTManager
from src.auth import auth_blueprint  
from src.web.controllers.api.routes import api_bp
from src.core.db import init_db_data  
import os
from dotenv import load_dotenv
from src.swagger_init import initialize_swagger
from src.web.controllers.api.planes import planes_blueprint

load_dotenv()

def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app)

    # Configura CORS
    CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "http://localhost:8080"}})

    # Cargar la configuración desde el objeto Config
    app.config.from_object(Config)

    # Inicializar la base de datos
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()
        init_db_data() 

    # Configura la clave secreta del JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Inicializar JWT Manager
    jwt = JWTManager(app)

    # Registrar el blueprint de autenticación
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(planes_blueprint, url_prefix='/api')

    # Registrar otras rutas de la API
    app.register_blueprint(api_bp, url_prefix='/api')

    initialize_swagger(app)
    
    return app