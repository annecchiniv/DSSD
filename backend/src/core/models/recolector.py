from src.core.db import db

class Recolector(db.Model):
    __tablename__ = "recolector"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    dni = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    active = db.Column(db.Boolean, default=True)
    
   # user_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))  # Cambia "user.id" a "usuario.id"
   # user = db.relationship("User", back_populates="recolector_asociation")  # Cambia a back_populates
  #  planes = db.relationship("PlanRecoleccion", secondary='plan_list')  # Asegúrate de que 'plan_list' esté definido

    def __init__(self, name, lastname, dni, email):
        self.name = name
        self.lastname = lastname
        self.dni = dni
        self.email = email


