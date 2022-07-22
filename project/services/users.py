import base64
import hashlib
import hmac

import jwt as jwt

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from project.dao.users import UserDAO
from constants import SECRET_KEY, ALGORITM


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one(self, uid):
        return self.user_dao.get_one(uid)

    def get_all(self):
        return self.user_dao.get_all()

    def get_user_by_email(self, email):
        return self.user_dao.get_user_by_email(email)

    def generate_user_password(self, password):
        hash_digest = self.get_hash(password)
        return base64.b64encode(hash_digest)

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

    def create(self, user):
        user['password'] = self.generate_user_password(user["password"])
        return self.user_dao.create_user(user)

    def compare_passwords(self, password_hash, other_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )

    def update(self, data):
        uid = data.get('id')
        user = self.get_one(uid)

        user.email = data.get('email')
        user.password = self.get_hash(data.get('password'))
        user.name = data.get('name')
        user.surname = data.get('surname')
        user.favorite_genre = data.get('favorite_genre')
        self.user_dao.update(user)

    def update_partial(self, data):
        uid = data.get('id')

        user = self.get_one(uid)

        if 'email' in data:
            user.email = data.get('email')
        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'password' in data:
            user.password = self.get_hash(data.get('password'))
        if 'favorite_genre' in data:
            user.favorite_genre = data.get('favorite_genre')

        return self.user_dao.update(user)

    def check_token(self, token):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITM])
