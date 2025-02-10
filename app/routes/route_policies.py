from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow.schema import Schema
from flask_jwt_extended import get_jwt, jwt_required
from marshmallow import fields
from datetime import datetime

from app.database import db
from app.schemas import SchemaPostPolicy, SchemaPolicy
from app.models import PolicyStatus, ModelPolicy, UserRole

blueprint_policies = Blueprint(
    "policies", "policies", url_prefix="/api/policies", description="Policies API")


@blueprint_policies.route("/policy/<string:id>")
class CollectionPolicyId(MethodView):
    @jwt_required()
    @blueprint_policies.response(status_code=200, schema=SchemaPolicy)
    def get(self, id):
        policy = db.session.query(ModelPolicy).filter_by(id=id).first()

        if not policy:
            return {"message": f"Policy not found - {id}"}, 404

        return policy


@blueprint_policies.route("/policy/active")
class CollectionPolicyStatus(MethodView):
    @jwt_required()
    @blueprint_policies.response(status_code=200, schema=SchemaPolicy)
    def get(self):
        policy = db.session.query(ModelPolicy).filter_by(
            status="ACTIVE").first()

        if not policy:
            return {"message": f"Policy not found - {id}"}, 404

        return policy


@blueprint_policies.route("/policy")
class CollectionPolicy(MethodView):
    @jwt_required()
    @blueprint_policies.arguments(SchemaPostPolicy, location="json")
    @blueprint_policies.response(status_code=201, schema=SchemaPolicy)
    def post(self, payload):
        user_claims = get_jwt()
        user_email = user_claims.get("email")
        user_role = user_claims.get("role")

        if user_role != UserRole.ADMIN.value:
            return f"Forbidden", 404
        if not user_email:
            return f"Forbidden", 404

        new_policy = ModelPolicy(
            status=PolicyStatus.INACTIVE,
            created_by=user_email,
            length=payload['length'],
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
            upper_case_length=payload['upper_case_length'],
            numbers_length=payload['numbers_length'],
            special_char_length=payload['special_char_length'],
        )

        db.session.add(new_policy)
        db.session.commit()

        return new_policy, 201
