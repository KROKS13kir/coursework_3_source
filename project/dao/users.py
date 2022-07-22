from project.dao.models.users import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create_user(self, user):
        user_ = User(**user)
        self.session.add(user_)
        self.session.commit()
        return user_

    def get_all(self):
        return self.session.query(User).all()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
        return user
