from marshmallow import Schema, fields

from project.setup_db import db
from project.dao.models.directors import DirectorSchema
from project.dao.models.genres import GenreSchema

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)

    genre = db.relationship("Genre")
    director = db.relationship("Director")


def __repr__(self):
        return f"<Movie '{self.title.title()}'>"



class MoviesSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)