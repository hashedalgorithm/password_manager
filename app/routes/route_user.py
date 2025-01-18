from flask.views import MethodView
from flask_smorest import Blueprint
from app.schemas import SchemaUser
from marshmallow import fields
from datetime import datetime


blueprint_user = Blueprint(
    "user", "user", url_prefix="/user", description="User API")


class ParamtersCollectionUserGet:
    user_id = fields.String()


@blueprint_user.route("/")
class CollectionUser(MethodView):

    @blueprint_user.arguments(ParamtersCollectionUserGet)
    @blueprint_user.response(status_code=200, schema=SchemaUser)
    def get(self, parameters) -> SchemaUser:
        return {
            "id": 1,
            "email": "sample@gmail.com",
            "name": "sample",
            "created_at": datetime.now
        }

    @blueprint_user.response(status_code=201, schema=SchemaUser)
    def post(self, user) -> SchemaUser:
        pass
