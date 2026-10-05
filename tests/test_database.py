from controle_exames.database.connection import connect, initialize_database


def test_initialization_is_idempotent_and_enables_foreign_keys(tmp_path):
    path = tmp_path / "nested" / "test.sqlite3"
    initialize_database(path)
    initialize_database(path)
    connection = connect(path)
    try:
        assert connection.execute("PRAGMA foreign_keys").fetchone()[0] == 1
        rows = connection.execute("SELECT value FROM app_metadata WHERE key = 'schema_version'").fetchall()
        assert len(rows) == 1
        assert rows[0]["value"] == "0"
    finally:
        connection.close()
