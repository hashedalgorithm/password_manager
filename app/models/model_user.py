from app.database import db
from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"


class ModelUser(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.USER)
    created_at = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<ModelUser id={self.id} email={self.email} name={self.name} role={self.role.value} created_at={self.created_at}>"
