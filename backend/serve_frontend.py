from flask import send_from_directory
from app import app 

@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend/dist', 'index.html')
