from src.core.db import db
from .planRecoleccion import PlanRecoleccion
from .recolector import Recolector

class Plan_List(db.Model):
    __tablename__ = "plan_list"
    
    id = db.Column(db.Integer, primary_key=True)
    #plan_id = db.Column(db.Integer, db.ForeignKey("planRecoleccion.id"), nullable=False)
   # recolector_id = db.Column(db.Integer, db.ForeignKey("recolector.id"), nullable=False)
    
    # Relaciones
    #plan = db.relationship("PlanRecoleccion", back_populates="planes_list")
    #recolector = db.relationship("Recolector", back_populates="planes")

    def __init__(self, plan_id, recolector_id):
        self.plan_id = plan_id
        self.recolector_id = recolector_id

