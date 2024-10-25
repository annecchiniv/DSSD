from src.core.db import db

class Orden(db.Model):
    __tablename__ = "orden"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre_orden = db.Column(db.String(100))
    reserva = db.Column(db.Boolean, default=False)
    deposito_id = db.Column(db.Integer, db.ForeignKey("deposito.id"))
    
    # Relación muchos a uno (una orden tiene un único depósito)
    deposito = db.relationship("Deposito", back_populates="ordenes")
    
    # Relación con la tabla intermedia
    ordenes_materiales = db.relationship("OrdenMaterial", back_populates="orden")