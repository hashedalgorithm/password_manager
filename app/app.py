from flask import Flask
from flask_smorest import Api
from app.config import APIConfig
from app.database import db
from app.services import init_tables
from app.routes import blueprint_users, blueprint_policies, blueprint_hibp

server = Flask(__name__)
server.config.from_object(APIConfig)

api = Api(server)

server.app_context().push()

db.init_app(server)

with server.app_context():
    db.create_all()
    init_tables(db)


api.register_blueprint(blueprint_users)
api.register_blueprint(blueprint_policies)
api.register_blueprint(blueprint_hibp)
