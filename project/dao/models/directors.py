from marshmallow import Schema, fields

from project.setup_db import db


class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Director '{self.name.title()}'>"


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()