from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from app.models.model_user import ModelUser
from datetime import datetime


def init_tables(db: SQLAlchemy):

    inti_users(db)

    db.session.commit()


def inti_users(db):
    db.session.execute(text('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    '''))
    admin = ModelUser(
        email='system@admin.com',
        name='admin',
        created_at=datetime.now().isoformat()
    )

    db.session.add(admin)

