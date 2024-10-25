from flask_sqlalchemy import SQLAlchemy
from src.core.models.deposito import Deposito
from src.core.models.material import Material

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    config_db(app)

def config_db(app):
    with app.app_context():
        db.create_all()  
        init_db() 

    @app.teardown_request
    def close_session(exception=None):
        db.session.remove()  

def reset_db():
    db.drop_all()
    db.create_all()

def init_db():
   
    if Deposito.query.count() == 0:
    
        depositos = [
            Deposito(nombre='Deposito 1'),
            Deposito(nombre='Deposito 2'),
            Deposito(nombre='Deposito 3')
        ]
        db.session.bulk_save_objects(depositos)
        
    if Material.query.count() == 0:
       
        materiales = [
            Material(nombre='Carton'),
            Material(nombre='Vidrio'),
            Material(nombre='Metal')
        ]
        db.session.bulk_save_objects(materiales)

    db.session.commit()
