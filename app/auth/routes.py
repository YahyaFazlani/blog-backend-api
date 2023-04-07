from app.auth import auth_bp
from flask import jsonify, request
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from flask_jwt_extended import create_access_token


@auth_bp.post("/signup")
def signup():
  data = request.get_json()
  print(data)

  # try:
  user = User.query.filter_by(email=data.get("email")).first()
  if not user:
    hashed_password = generate_password_hash(
        data["password"], method="sha256")
    data.pop("password")

    user = User(**data, password=hashed_password)

    db.session.add(user)
    db.session.commit()
    access_token = create_access_token(identity=user.id)

    return jsonify(token=access_token), 203
  else:
    return jsonify(status="fail", message="User already exists"), 409
  # except Exception:
  #   return jsonify(message="An error occurred"), 401


@auth_bp.post("/signin")
def signin():
  data = request.get_json()

  if not data or not data["email"] or not data["password"]:
    return jsonify({"status": "fail", "message": "Could not verify due to insufficient data"}), 401

  user = User.query.filter_by(email=data["email"]).first()
  if check_password_hash(user.password, data["password"]):
    access_token = create_access_token(identity=user.id)
    return jsonify(token=access_token)

  else:
    return jsonify(status="fail", message="User not found"), 404
