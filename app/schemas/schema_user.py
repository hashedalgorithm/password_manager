from marshmallow.schema import Schema
from marshmallow import fields
from app.models import UserRole


class SchemaPostUser(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    role = fields.Enum(UserRole, required=True)


class SchemaGetUser(Schema):
    email = fields.Email(required=True)
    role = fields.Enum(UserRole, required=True)
    token = fields.String(required=True)


class SchemaUser(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    name = fields.String(required=True)
    role = fields.Enum(UserRole, required=True)
    created_at = fields.String(required=True)
