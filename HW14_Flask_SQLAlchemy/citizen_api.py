import http
from database import db
from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError

from models.citizen import Citizen
from serializers.citizen import CitizenSchema

citizen_router = Blueprint('citizen', __name__, url_prefix='/citizen')


@citizen_router.route('/')
def get():
    citizen_schema = CitizenSchema()

    citizens = Citizen.query.order_by(Citizen.iin)  # users = User.query.order(User.email)
    # users = User.query.order_by(email=email)
    citizens_json = citizen_schema.dump(citizens, many=True)
    return jsonify(citizens_json)
    # User.query.filter().order(User.id)
    # print(users)
    # print(users[0].__dict__)


@citizen_router.route('/<int:id_>')
def retrieve(id_):
    citizen_schema = CitizenSchema()
    citizen = Citizen.query.filter_by(id=id_).first()  # user = User.query.filter(User.id == id_).first()
    citizens_json = citizen_schema.dump(citizen)
    return jsonify(citizens_json)


@citizen_router.route('/', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = CitizenSchema()
    try:
        citizen_data = schema.load(data)
        new_citizen = Citizen(iin=citizen_data['iin'],
                              full_name=citizen_data['full_name'])
        db.session.add(new_citizen)
        db.session.commit()

        new_citizen_json = schema.dump(new_citizen)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_citizen_json


@citizen_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = CitizenSchema()
    try:
        citizen_data = schema.load(data)
        citizen = Citizen.query.filter_by(id=id_).first()
        citizen.iin = citizen_data['iin']
        citizen.full_name = citizen_data['full_name']
        db.session.add(citizen)
        db.session.commit()

        new_citizen_json = schema.dump(citizen)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_citizen_json


@citizen_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Citizen.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
