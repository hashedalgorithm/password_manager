from marshmallow.schema import Schema
from marshmallow import fields


class SchemaPostUser(Schema):
    email = fields.String(required=True)
    name = fields.String(required=True)


class SchemaUser(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    name = fields.String(required=True)
    created_at = fields.DateTime(required=True)
