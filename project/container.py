from project.dao.directors import DirectorDAO
from project.dao.genres import GenreDAO
from project.dao.movies import MoviesDao
from project.dao.users import UserDAO
from project.services.auth import AuthService
from project.services.directors import DirectorsService
from project.services.genres import GenreService
from project.services.movies import MoviesService
from project.services.users import UserService
from project.setup_db import db


genre_dao = GenreDAO(session=db.session)
movie_dao = MoviesDao(session=db.session)
director_dao = DirectorDAO(session=db.session)
user_dao = UserDAO(session=db.session)

genre_service = GenreService(genre_dao=genre_dao)
movie_service = MoviesService(movies_dao=movie_dao)
director_service = DirectorsService(directors_dao=director_dao)
user_service = UserService(user_dao=user_dao)
auth_service = AuthService(user_service)