from flask import Flask
from app.routes import home_routes, about_routes
from app.middleware import before_request_middleware

def create_app():
    app = Flask(__name__)

    # Register blueprints (routes)
    app.register_blueprint(home_routes.bp)
    app.register_blueprint(about_routes.bp)

    # Register middleware
    app.before_request(before_request_middleware)
    print("Middleware registered")

    return app