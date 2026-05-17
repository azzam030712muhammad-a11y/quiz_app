from flask import Flask
from web.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecretkey"

    register_routes(app)

    return app