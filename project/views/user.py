from flask import request, abort
from flask_restx import Resource, Namespace

from project.dao.models.users import UsersSchema
from project.container import user_service
from project.tools.security import auth_required

user_ns = Namespace('users')


@user_ns.route('/', methods=['GET', 'PATCH'])
class UserView(Resource):
    @auth_required
    def get(self):
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        email = user_service.check_token(token)['email']
        user = user_service.get_user_by_email(email)
        if user:
            return UsersSchema().dump(user), 200
        return {'message': 'Object not found'}, 400

    @auth_required
    def patch(self):
        req_json = request.json
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        email = user_service.check_token(token)['email']
        user = user_service.get_user_by_email(email)
        uid = user.id
        req_json['id'] = uid
        user = user_service.update_partial(req_json)
        if user:
            return {'message': 'Object updated'}, 204
        return {'message': 'Object not found'}, 400


@user_ns.route('/password')
class UserView(Resource):
    @auth_required
    def put(self):
        req_json = request.json
        old_password = req_json['password_1']
        new_password = req_json['password_2']
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        email = user_service.check_token(token)['email']
        user = user_service.get_user_by_email(email)
        uid = user.id

        data = {'id': uid, 'password': new_password}

        try:
            status = user_service.compare_passwords(user.password, old_password)
            if status:
                user_service.update_partial(data)
                return {'message': 'Password changed'}, 200
            else:
                abort(401)
        except Exception as e:
            abort(401, message=str(e))
