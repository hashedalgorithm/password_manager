from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from app.config import APIConfig
from app.database import db
from app.services import init_tables
from app.routes import blueprint_users, blueprint_policies, blueprint_hibp, blueprint_password

server = Flask(__name__)
server.config.from_object(APIConfig)
jwt = JWTManager(server)

api = Api(server)

server.app_context().push()

db.init_app(server)

with server.app_context():
    db.create_all()
    init_tables(db)


api.register_blueprint(blueprint_users)
api.register_blueprint(blueprint_policies)
api.register_blueprint(blueprint_hibp)
api.register_blueprint(blueprint_password)
