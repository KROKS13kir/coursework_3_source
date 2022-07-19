from flask import request
from flask_restx import Resource, Namespace

from project.container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegister(Resource):
    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@auth_ns.route('/login/')
class AuthLogin(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in (email, password):
            return "", 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens

    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")
        return auth_service.approve_refresh_token(token), 201