from src.core.db import db

class DepositoMaterial(db.Model):
    __tablename__ = "deposito_material"
    
    id = db.Column(db.Integer, primary_key=True)
    deposito_id = db.Column(db.Integer, db.ForeignKey("deposito.id"), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey("material.id"), nullable=False)

    # Relación con Deposito y Material
    deposito = db.relationship("Deposito", back_populates="depositos_materiales")
    material = db.relationship("Material", back_populates="depositos_materiales")
