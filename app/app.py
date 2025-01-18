from flask import Flask
from flask_smorest import Api
from app.config import APIConfig
from app.routes.route_user import blueprint_user

server = Flask(__name__)
server.config.from_object(APIConfig)

api = Api(server)

api.register_blueprint(blueprint_user)
