from flask import Flask, render_template
from flask_restx import Api

from project.views.auth.auth import auth_ns
from project.views.directors import directors_ns
from project.views.genres import genres_ns
from project.views.movies import movie_ns
from project.config import BaseConfig
from project.setup_db import db
from project.views.user import user_ns
from flask_cors import CORS

api = Api(title="Flask Course Project 3", doc="/docs")


def create_app(*args):
    application = Flask(__name__)
    application.config.from_object(args)

    @application.route('/')
    def index():
        return render_template('index.html')

    register_extensions(application)

    CORS(app=application)

    return application


def register_extensions(application):
    db.init_app(application)
    api.init_app(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


if __name__ == '__main__':
    app_config = BaseConfig()
    app = create_app(app_config)
    app.run(port=25000)