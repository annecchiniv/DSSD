from flask import send_from_directory
import os

def serve_frontend(app):
    @app.route('/')
    def serve_index():
        dist_path = os.path.join(app.root_path, '../frontend/dist')
        return send_from_directory('../frontend/dist', 'index.html')
