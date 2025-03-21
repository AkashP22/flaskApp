from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import datetime

bp = Blueprint('auth', __name__)

# Dummy users (Replace this with a database later)
users = {
    "akash": "password123",
    "admin": "admin123"
}

# Login Route (Generate JWT Token)
@bp.route("/login", methods=["POST"])
def login():
    
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    print("Login route", username, password)

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(hours=1))
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid username or password"}), 401

# Protected Route (Requires JWT)
@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f"Hello, {current_user}! This is a protected route."), 200