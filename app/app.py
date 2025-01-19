from flask import Flask
from flask_smorest import Api
from app.config import APIConfig
from app.routes.route_users import blueprint_users
from app.services.service_database import init_tables
from app.database import db

server = Flask(__name__)
server.config.from_object(APIConfig)

api = Api(server)

server.app_context().push()

db.init_app(server)

with server.app_context():
    db.create_all()
    init_tables(db)


api.register_blueprint(blueprint_users)
