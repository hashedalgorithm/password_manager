from datetime import datetime
from app.app import db
from enum import Enum


class PolicyStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class ModelPolicy(db.Model):
    __tablename__ = "policies"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(PolicyStatus), nullable=False,
                       default=PolicyStatus.INACTIVE.value)
    created_at = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.String(100), nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    length = db.Column(db.Integer, nullable=False, default=12)
    upper_case_length = db.Column(db.Integer, nullable=False, default=2)
    numbers_length = db.Column(db.Integer, nullable=False, default=2)
    special_char_length = db.Column(db.Integer, nullable=False, default=2)
