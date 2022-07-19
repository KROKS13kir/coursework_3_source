from marshmallow import Schema, fields

from project.setup_db import db

class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"

class GenreSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)