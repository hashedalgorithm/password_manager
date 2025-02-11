from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime
from app.models.model_policy import ModelPolicy, PolicyStatus
from app.models.model_user import ModelUser, UserRole


def init_tables(db: SQLAlchemy):

    inti_users(db)
    init_policies(db)
    init_password(db)

    db.session.commit()


def inti_users(db):
    db.session.execute(text('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    '''))

    existing_admin = db.session.execute(text(
        'SELECT * FROM users WHERE email = :email'), {'email': 'system@admin.com'}).fetchone()
    if not existing_admin:
        admin = ModelUser(
            email='system@admin.com',
            name='admin',
            role=UserRole.ADMIN,
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
            special_char_length INTEGER NOT NULL
        )
    '''))

    existing_policy = db.session.execute(text(
        'SELECT * FROM policies WHERE status = :status'), {'status': PolicyStatus.ACTIVE.name}).fetchone()

    if not existing_policy:
        default_policy = ModelPolicy(
            length=12,
            upper_case_length=2,
            numbers_length=2,
            status=PolicyStatus.ACTIVE,
            special_char_length=2,
            created_by='system',
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        db.session.add(default_policy)


def init_password(db):
    db.session.execute(text('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password_hash TEXT NOT NULL,
            account_provider TEXT NOT NULL,
            account_provider_email TEXT,
            user_email TEXT NOT NULL,
            policy_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(user_email) REFERENCES users(email),
            FOREIGN KEY(policy_id) REFERENCES policies(id)
        )
    '''))
