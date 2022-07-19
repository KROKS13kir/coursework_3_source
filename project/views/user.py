from flask import request
from flask_restx import Resource, Namespace

from project.dao.models.users import UsersSchema
from project.container import user_service
from project.tools.security import auth_required

user_ns = Namespace('users')


@user_ns.route("/<int:uid>/")
class UserView(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UsersSchema().dump(user)
        return result, 200

    @auth_required
    def patch(self, uid):
        data = request.get_json()
        user_service.update_part(data, uid)
        return '', 204

    @auth_required
    def put(self, uid):
        req_json = request.json
        user_service.update(req_json, uid)
        return "", 204