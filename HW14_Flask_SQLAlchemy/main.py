import http

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#psycopg2

from config import Config
from database import db
from citizen_api import citizen_router

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)  #db = SQLAlchemy()
    # db.create_all()
    # db.session.commit()
    app.register_blueprint(citizen_router)
    return app


def setup_db(app):
    with app.app_context():
        db.create_all()
        db.session.commit()


if __name__ == '__main__':
    app = create_app()
    # db.session.add(User(email="andrii@gmail.com"))
    # db.session.commit()
    #print(db)
    setup_db(app)
    app.run(host="0.0.0.0")