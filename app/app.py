from flask import Flask
from flask_smorest import Api, Blueprint
from app.config import APIConfig

server = Flask(__name__)
server.config.from_object(APIConfig)

api = Api(server)

blueprint_user = Blueprint(
    "user", "user", url_prefix="/user", description="User API")

api.register_blueprint(blueprint_user)
