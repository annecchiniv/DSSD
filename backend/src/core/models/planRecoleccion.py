from src.core.db import db

class PlanRecoleccion(db.Model):
    __tablename__ = "planRecoleccion"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre_plan = db.Column(db.String(100))
    tipo_material = db.Column(db.String(20))
    cantidad = db.Column(db.Integer)
    area_recoleccion = db.Column(db.String(100))
    
    # Relación con Plan_List
    #planes_list = db.relationship("Plan_List", back_populates="plan", cascade="all, delete-orphan")

    def __init__(self, nombre_plan, tipo_material, cantidad, area_recoleccion):
        self.nombre_plan = nombre_plan
        self.tipo_material = tipo_material
        self.cantidad = cantidad
        self.area_recoleccion = area_recoleccion

    def create(plan):
        db.session.add(plan)
        db.session.commit()
        return plan