from src.core.db import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(256)) 
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50)) 
    #state = db.Column(db.Boolean, default=True) 
    #dni = db.Column(db.String(20), unique=True)
    #recolector_asociation = db.relationship("Recolector")
    #auditor_asociation = db.relationship("Auditor", back_populates="user")

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = generate_password_hash(password)

    