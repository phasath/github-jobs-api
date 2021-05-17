from flask_sqlalchemy import SQLAlchemy

from app.core.config import Config
from app.util.requests import get_requests_session


CONFIG = Config()
REQUESTS = get_requests_session()

DB_ENGINE_OPTIONS = {
    "convert_unicode": True,
    "echo": CONFIG.IS_LOCAL,
    "pool_recycle": 3600,
}

DB_SESSION_OPTIONS = {
    "autocommit": False,
    "autoflush": False,
}

DB = SQLAlchemy(
    engine_options=DB_ENGINE_OPTIONS,
    session_options=DB_SESSION_OPTIONS,
)

__all__ = ["CONFIG", "REQUESTS"]
