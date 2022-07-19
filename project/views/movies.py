from flask import request

from project.container import movie_service
from project.dao.models.movies import MoviesSchema
from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        page = request.args.get('page', type=int)
        status = request.args.get('status')
        movies = movie_service.get_all(page, status)
        return MoviesSchema(many=True).dump(movies), 200


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):
    def get(self, mid):
        b = movie_service.get_one(mid)
        sm_d = MoviesSchema().dump(b)
        return sm_d, 200