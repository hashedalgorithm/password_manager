from marshmallow.schema import Schema
from marshmallow import fields
from app.models import PolicyStatus


class SchemaPostPolicy(Schema):
    length = fields.Int(required=True, default=12)
    upper_case_length = fields.Int(required=True, default=2)
    numbers_length = fields.Int(required=True, default=2)
    special_char_length = fields.Int(required=True, default=2)


class SchemaPolicy(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Enum(PolicyStatus, required=True)
    created_at = fields.String(required=True)
    updated_at = fields.String(required=True)
    created_by = fields.String(required=True)
    length = fields.Int(required=True, default=12)
    upper_case_length = fields.Int(required=True, default=2)
    numbers_length = fields.Int(required=True, default=2)
    special_char_length = fields.Int(required=True, default=2)
