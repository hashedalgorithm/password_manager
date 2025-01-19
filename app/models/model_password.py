from app.app import db
from datetime import datetime


class ModelPassword(db.Model):
    __tablename__ = "passwords"

    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    account_provider = db.Column(db.String(128), nullable=False)
    account_provider_email = db.Column(db.String(128), nullable=True)
    account_provider_username = db.Column(db.String(128), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_email = db.Column(db.String(100), db.ForeignKey(
        'users.email'), nullable=False)
    policy_id = db.Column(db.Integer, db.ForeignKey(
        'policies.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ModelPassword(id={self.id}, password_hash={self.password_hash}, account_provider={self.account_provider}, account_provider_email={self.account_provider_email}, account_provider_username={self.account_provider_username}, user_id={self.user_id}, user_email={self.user_email}, policy_id={self.policy_id}, created_at={self.created_at}, updated_at={self.updated_at})>"
