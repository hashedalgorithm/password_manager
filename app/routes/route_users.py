from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow.schema import Schema
from marshmallow import fields
from datetime import datetime
from app.database import db
from app.schemas import SchemaUser, SchemaPostUser, SchemaGetUser
from app.models import UserRole, ModelUser
from flask_jwt_extended import create_access_token

blueprint_users = Blueprint(
    "users", "users", url_prefix="/api/users", description="User API")


@blueprint_users.route("/user/<string:email>")
class CollectionUserId(MethodView):

    @blueprint_users.response(status_code=200, schema=SchemaGetUser)
    def get(self, email):
        user = db.session.query(ModelUser).filter_by(email=email).first()

        if not user:
            return {"message": f"User not found - {email}"}, 404

        access_token = create_access_token(identity=user.email)
        return {"email": email, "role": user.role, "token": access_token}


@blueprint_users.route("/user")
class CollectionUser(MethodView):

    @blueprint_users.arguments(SchemaPostUser, location="json")
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
