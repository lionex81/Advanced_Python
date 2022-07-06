from marshmallow import Schema, fields
from marshmallow.validate import Length


class CitizenSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    iin = fields.Integer(required=True)  #validate=Length(min=10, max=10)
    full_name = fields.String(required=True)
    # password = fields.String(required=True, load_only=True)


