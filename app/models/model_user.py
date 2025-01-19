from app.app import db


class ModelUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<ModelUser id={self.id} email={self.email} name={self.name} created_at={self.created_at}>"
