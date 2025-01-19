from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


def init_tables(db: SQLAlchemy):
    db.session.execute(text('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    '''))

    db.session.commit()
