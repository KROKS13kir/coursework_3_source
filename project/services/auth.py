import jwt
import datetime
import calendar

from my_constants import SECRET_KEY, ALGORITM


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_user_by_email(email)

        if not user:
            raise Exception()

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise Exception()

        data = {
            "email": user.email
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITM)

        days_130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days_130.timetuple())
        refresh_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=SECRET_KEY, algorithms=ALGORITM)
        email = data["email"]

        user = self.user_service.get_user_by_email(email)

        if not user:
            raise Exception()
        return self.generate_tokens(user.email, user.password, is_refresh=True)