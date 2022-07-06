from database import db


class Citizen(db.Model):
    __tablename__ = 'citizens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    iin = db.Column(db.Integer, nullable=False, unique=True)
    full_name = db.Column(db.String(300), nullable=False)