from src.core.db import db

class Deposito(db.Model):
    __tablename__ = "deposito"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(50))
    ubicacion=db.Column(db.String(100))
 
    
    # Relación uno a muchos con Orden
    ordenes = db.relationship("Orden", back_populates="deposito")
    
    # Relación muchos a muchos con Material (a través de la tabla intermedia)
    depositos_materiales = db.relationship("DepositoMaterial", back_populates="deposito")