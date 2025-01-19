from flask.views import MethodView
from flask_smorest import Blueprint
from app.schemas import SchemaUser
from marshmallow.schema import Schema
from marshmallow import fields
from datetime import datetime
from app.database import db
from app.models.model_user import UserRole, ModelUser

blueprint_users = Blueprint(
    "users", "users", url_prefix="/api/users", description="User API")


class ParamtersCollectionUserGet(Schema):
    user_id = fields.String()


class ParametersCollectionUsersPost(Schema):
    name = fields.String()
    email = fields.String()
    role = fields.Enum(UserRole)


@blueprint_users.route("/user/<string:email>")
class CollectionUser(MethodView):

    @blueprint_users.response(status_code=200, schema=SchemaUser)
    def get(self, email):
        user = db.session.query(ModelUser).filter_by(email=email).first()

        if not user:
            return {"message": f"User not found - {email}"}, 404

        return user


@blueprint_users.route("/user")
class CollectionUser(MethodView):

    @blueprint_users.arguments(ParametersCollectionUsersPost, location="json")
    @blueprint_users.response(status_code=201, schema=SchemaUser)
    def post(self, user):
        new_user = ModelUser(
            email=user['email'],
            name=user['name'],
            created_at=datetime.now().isoformat()
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user, 201
