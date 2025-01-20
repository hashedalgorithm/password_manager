from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow.schema import Schema
from marshmallow import fields
from datetime import datetime
from app.database import db
from app.services import check_if_password_is_leaked


blueprint_hibp = Blueprint(
    "Have I been pawned", "HIBP", url_prefix="/api/hibp", description="HIBP API")


@blueprint_hibp.route("/check/<string:password>")
class CollectionHIBP(MethodView):

    @blueprint_hibp.response(status_code=200)
    def get(self, password):
        result = check_if_password_is_leaked(password)

        return {
            "leaked": result
        }
