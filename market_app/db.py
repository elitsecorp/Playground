import sqlite3
from pathlib import Path

from flask import current_app, g


def get_db():
    if "db" not in g:
        db_path = Path(current_app.config["DATABASE"])
        db_path.parent.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
        ensure_initialized(g.db)
    return g.db


def ensure_columns(db):
    migrations = {
        "companies": [
            ("contact_phone", "TEXT NOT NULL DEFAULT ''"),
            ("contact_email", "TEXT NOT NULL DEFAULT ''"),
            ("contact_address", "TEXT NOT NULL DEFAULT ''"),
            ("investor_notes", "TEXT NOT NULL DEFAULT ''"),
        ],
        "scores": [
            ("eps", "REAL NOT NULL DEFAULT 0"),
            ("implied_pe", "REAL NOT NULL DEFAULT 0"),
            ("current_price", "REAL NOT NULL DEFAULT 0"),
            ("target_price_for_20pc", "REAL NOT NULL DEFAULT 0"),
        ],
    }
    for table, columns in migrations.items():
        existing_columns = {
            row[1] for row in db.execute(f"PRAGMA table_info({table})").fetchall()
        }
        for column, definition in columns:
            if column not in existing_columns:
                db.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


def ensure_initialized(db):
    exists = db.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'companies'"
    ).fetchone()
    if not exists:
        for filename in ("schema.sql", "seed.sql"):
            script_path = Path(__file__).with_name(filename)
            db.executescript(script_path.read_text(encoding="utf-8"))
        db.commit()
    ensure_columns(db)


def close_db(_error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def run_script(filename):
    db = get_db()
    script_path = Path(__file__).with_name(filename)
    db.executescript(script_path.read_text(encoding="utf-8"))
    db.commit()


def init_db():
    run_script("schema.sql")
    run_script("seed.sql")


def init_app(app):
    @app.cli.command("init-db")
    def init_db_command():
        init_db()
        print("Initialized the database.")
