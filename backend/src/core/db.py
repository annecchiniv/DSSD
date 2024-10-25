from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    #config_db(app)

"""
def config_db(app):
    with app.app_context():
        print("1")
        db.create_all()  # Crea las tablas
        print("2")
        init_db_data()  # Llama a la función para inicializar los datos
        print("3")
"""
def reset_db():
    with app.app_context():
        db.drop_all()  
        db.create_all()  
        init_db_data()  

def init_db_data():
    from src.core.models.deposito import Deposito
    from src.core.models.material import Material

    if Deposito.query.count() == 0:
        depositos = [
            Deposito(nombre='Deposito 1', ubicacion='Ubicación 1'),
            Deposito(nombre='Deposito 2', ubicacion='Ubicación 2'),
            Deposito(nombre='Deposito 3', ubicacion='Ubicación 3')
        ]
        for deposito in depositos:
            db.session.add(deposito) 

        
    if Material.query.count() == 0:
        materiales = [
            Material(nombre='Carton'),
            Material(nombre='Vidrio'),
            Material(nombre='Metal')
        ]
        for material in materiales:
            db.session.add(material) 

    db.session.commit()
