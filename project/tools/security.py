import hashlib
import jwt
from flask import request
from flask_restx import abort
from constants import SECRET_KEY, ALGORITM
from flask import current_app


def generate_password_digest(password):
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )

def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(403)
        return func(*args, **kwargs)

    return wrapper
