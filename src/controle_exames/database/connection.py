import sqlite3
from pathlib import Path


def connect(path: str | Path) -> sqlite3.Connection:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database(path: str | Path) -> None:
    connection = connect(path)
    try:
        with connection:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS app_metadata "
                "(key TEXT PRIMARY KEY, value TEXT NOT NULL)"
            )
            connection.execute(
                "INSERT OR IGNORE INTO app_metadata (key, value) VALUES (?, ?)",
                ("schema_version", "0"),
            )
    finally:
        connection.close()
