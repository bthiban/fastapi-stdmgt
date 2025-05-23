from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_NAME = os.getenv("MYSQL_DB")

# Fallback to SQLite in-memory for test/CI
_tmp_db_url: str

if all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
    _tmp_db_url = (
        f"mysql+asyncmy://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
else:
    _tmp_db_url = "sqlite+aiosqlite:///:memory:"

DATABASE_URL = _tmp_db_url
