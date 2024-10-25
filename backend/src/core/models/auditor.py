from src.core.db import db

class Auditor(db.Model):
    __tablename__ = "auditor"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50)) 
    lastname = db.Column(db.String(50))  
    dni = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True) 
    active = db.Column(db.Boolean, default=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("usuario.id")) 
    #user = db.relationship("User", back_populates="auditor_asociation")


    
