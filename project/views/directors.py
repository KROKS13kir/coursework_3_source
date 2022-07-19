from flask_restx import Resource, Namespace
from project.container import director_service
from project.dao.models.directors import DirectorSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@directors_ns.route('/<int:did>/')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        result = DirectorSchema().dump(director)
        return result, 200