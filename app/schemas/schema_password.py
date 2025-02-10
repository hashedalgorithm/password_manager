from marshmallow.schema import Schema
from marshmallow import fields


class SchemaPassword(Schema):
    id = fields.Int(dump_only=True)
    password_hash = fields.String(required=True)
    account_provider = fields.String(required=True)
    account_provider_email = fields.String(required=True)
    user_email = fields.String(required=True)
    policy_id = fields.Int(dump_only=True)
    created_at = fields.String(dump_only=True)
    updated_at = fields.String(dump_only=True)


class SchemaPostPasswordRequest(Schema):
    account_provider = fields.String(required=True)
    account_provider_email = fields.String(required=True)


class SchemaPostPasswordResponse(Schema):
    account_provider = fields.String(required=True)
    account_provider_email = fields.String(required=True)
    password = fields.String(required=True)
