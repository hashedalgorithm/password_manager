from flask.views import MethodView
from flask_smorest import Blueprint
from app.schemas import SchemaUser
from marshmallow.schema import Schema
from marshmallow import fields
from datetime import datetime

users = [{
    "id": 1,
    "email": "sample@gmail.com",
    "name": "sample",
    "created_at": datetime.now().isoformat()
}]

blueprint_users = Blueprint(
    "user", "user", url_prefix="/api/users", description="User API")


class ParamtersCollectionUserGet(Schema):
    user_id = fields.String()


@blueprint_users.route("/")
class CollectionUsers(MethodView):

    @blueprint_users.arguments(ParamtersCollectionUserGet, location="query")
    @blueprint_users.response(status_code=200, schema=SchemaUser)
    def get(self, parameters):
        user_id = parameters['user_id']

        return next((user for user in users if user["id"] == int(user_id)), None)

    @blueprint_users.response(status_code=201, schema=SchemaUser)
    def post(self, user):
        pass
