from marshmallow import Schema, fields

from project.dao.models.genres import Genre
from project.setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.String, db.ForeignKey(Genre.id), nullable=False)

    def __repr__(self):
        return f"<User '{self.email}'>"


class UsersSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()