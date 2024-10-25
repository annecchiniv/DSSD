from src.core.db import db

class Material(db.Model):
    __tablename__ = "material"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(20))
#    cant = db.Column(db.Integer)
    
    # Relación muchos a muchos con Deposito (a través de la tabla intermedia)
    depositos_materiales = db.relationship("DepositoMaterial", back_populates="material")
    
    # Relación con la tabla intermedia
    ordenes_materiales = db.relationship("OrdenMaterial", back_populates="material")
    
   # planes = db.relationship("PlanRecoleccion", back_populates="materiales")  # Asegúrate de definir la relación en PlanRecoleccion
def __init__(self, name, ):
        self.name = name