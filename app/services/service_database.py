from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from app.models.model_policy import ModelPolicy
from app.models.model_user import ModelUser
from datetime import datetime


def init_tables(db: SQLAlchemy):

    inti_users(db)
    init_policies(db)

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


def init_policies(db):
    db.session.execute(text('''
        CREATE TABLE IF NOT EXISTS policies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            created_by TEXT NOT NULL,
            length INTEGER NOT NULL,
            upper_case_length INTEGER NOT NULL,
            numbers_length INTEGER NOT NULL,
            special_char_length INTEGER NOT NULL,
        )
    '''))
    default_policy = ModelPolicy(
        length=12,
        upper_case_length=2,
        numbers_length=2,
        status="active",
        special_char_length=2,
        created_by='system',
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat()
    )

    db.session.add(default_policy)
