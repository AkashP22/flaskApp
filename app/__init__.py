from flask import Flask
from app.routes import home_routes, about_routes, auth_routes
from app.middleware import before_request_middleware
from flask_jwt_extended import JWTManager
from config import Config
import os

def create_app():
    app = Flask(__name__)
    # Set secret keys from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
     
    # Initialize JWT
    jwt = JWTManager(app)
    # secret_key = os.urandom(16)
    # print('secret_key', secret_key)
    # hex_key = secret_key.hex()
    # print('hex_key', hex_key)


    # Register blueprints (routes)
    app.register_blueprint(home_routes.bp)
    app.register_blueprint(about_routes.bp)
    app.register_blueprint(auth_routes.bp) 

    # Register middleware
    app.before_request(before_request_middleware)
    print("Middleware registered")

    return app