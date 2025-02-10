from flask import Blueprint, jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from app.schemas import SchemaPassword, SchemaPostPasswordRequest, SchemaPostPasswordResponse
from app.models import ModelPassword, ModelPolicy
from app.services import generatePassword
from bcrypt import hashpw, gensalt

blueprint_password = Blueprint(
    'passwords', "passwords", url_prefix="/api/passwords", description="Passwords API")


@blueprint_password.route("/generate")
class CollectionPasswords(MethodView):

    @blueprint_password.arguments(SchemaPostPasswordRequest, location="json")
    @blueprint_password.response(status_code=201, schema=SchemaPostPasswordResponse)
    def post(self, password):
        verify_jwt_in_request()
        user_claims = get_jwt_identity()
        user_email = user_claims.get("email")

        if not user_email:
            return f"Forbidden", 500

        active_policy = ModelPolicy.query.filter_by(status="active").first()

        if not active_policy:
            return f"Internal Server Error", 500

        generated_password = generatePassword(active_policy.length, active_policy.upper_case_length,
                                              active_policy.numbers_length, active_policy.special_char_length)

        hashed_password = hashpw(generated_password.encode('utf-8'), gensalt())

        new_entry = ModelPassword(
            password_hash=hashed_password,
            account_provider=password["account_provider"],
            account_provider_email=password["account_provider_email"],
            user_email=user_email,
            policy_id=active_policy['id']
        )

        db.session.add(new_entry)
        db.session.commit()

        return {account_provider: password["account_provider"], account_provider_email: password['account_provider_email'], password: generated_password}
