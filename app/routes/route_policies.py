from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow.schema import Schema
from marshmallow import fields
from datetime import datetime
from app.database import db
from app.schemas import SchemaPostPolicy, SchemaPolicy
from app.models import PolicyStatus, ModelPolicy

blueprint_policies = Blueprint(
    "policies", "policies", url_prefix="/api/policies", description="Policies API")


@blueprint_policies.route("/policy/<string:id>")
class CollectionPolicyId(MethodView):

    @blueprint_policies.response(status_code=200, schema=SchemaPolicy)
    def get(self, id):
        policy = db.session.query(ModelPolicy).filter_by(id=id).first()

        if not policy:
            return {"message": f"Policy not found - {id}"}, 404

        return policy


@blueprint_policies.route("/policy/active")
class CollectionPolicyStatus(MethodView):

    @blueprint_policies.response(status_code=200, schema=SchemaPolicy)
    def get(self, status):
        policy = db.session.query(ModelPolicy).filter_by(
            status="ACTIVE").first()

        if not policy:
            return {"message": f"Policy not found - {id}"}, 404

        return policy


@blueprint_policies.route("/policy")
class CollectionPolicy(MethodView):

    @blueprint_policies.arguments(SchemaPostPolicy, location="json")
    @blueprint_policies.response(status_code=201, schema=SchemaPolicy)
    def post(self, policy):
        new_policy = ModelPolicy(
            status='inactive',
            created_by=policy['created_by'],
            length=policy['length'],
            upper_case_length=policy['upper_case_length'],
            numbers_length=policy['numbers_length'],
            special_char_length=policy['special_char_length'],
        )

        db.session.add(new_policy)
        db.session.commit()

        return new_policy, 201
