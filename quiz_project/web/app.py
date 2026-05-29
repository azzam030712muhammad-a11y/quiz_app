from flask import Flask
from web.routes import register_routes

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static"
    )

    app.secret_key = "supersecretkey"
    

    register_routes(app)

    return app