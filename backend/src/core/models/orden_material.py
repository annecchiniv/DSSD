from src.core.db import db

class OrdenMaterial(db.Model):
    __tablename__ = "orden_material"
    
    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey("orden.id"), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey("material.id"), nullable=False)
    
    # Atributos adicionales en la relación
    cantidad = db.Column(db.Integer, nullable=False)
    
    # Relaciones con Orden y Material
    orden = db.relationship("Orden", back_populates="ordenes_materiales")
    material = db.relationship("Material", back_populates="ordenes_materiales")
