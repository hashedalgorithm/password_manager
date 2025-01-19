from flask import Flask
from flask_smorest import Api
from app.config import APIConfig
from app.routes.route_user import blueprint_user
from flask_sqlalchemy import SQLAlchemy


server = Flask(__name__)
server.config.from_object(APIConfig)

api = Api(server)

server.app_context().push()

db = SQLAlchemy(server)

with server.app_context():
    db.create_all()


api.register_blueprint(blueprint_user)
