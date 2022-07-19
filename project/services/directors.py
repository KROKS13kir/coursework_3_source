from project.dao.directors import DirectorDAO


class DirectorsService:
    def __init__(self, directors_dao: DirectorDAO):
        self.directors_dao = directors_dao

    def get_one(self, did):
        return self.directors_dao.get_one(did)

    def get_all(self):
        return self.directors_dao.get_all()

