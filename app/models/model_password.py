from app.app import db
from datetime import datetime


class ModelPassword(db.Model):
    __tablename__ = "password"

    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    account_provider = db.Column(db.String(128), nullable=False)
    account_provider_email = db.Column(db.String(128), nullable=True)
    account_provider_username = db.Column(db.String(128), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
