"""Configures the application
"""
import os


def get_psql_conn_string():
    host = os.environ.get("PGHOST", "postgres")
    db = os.environ.get("PGDATABASE", "jobs4you")
    port = os.environ.get("PGPORT", "5432")
    username = os.environ.get("PGUSER", "jobs4you")
    password = os.environ.get("PGPASSWORD", "27613123j0b54You97402234")
    url = os.environ.get("PGCONNURL", None)
    return url or f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"


def get_redis_conn_string():
    host = os.environ.get("CACHE_REDIS_HOST", "redis")
    db = os.environ.get("CACHE_REDIS_DB", "0")
    port = os.environ.get("CACHE_REDIS_PORT", "6379")
    url = os.environ.get("CACHE_REDIS_URL", None)
    return url or f"redis://{host}:{port}/{db}"


class Config:
    APP_ENV = os.environ.get("APP_ENV", default="development")
    BASIC_AUTH_USERNAME = os.environ.get(
        "BASIC_AUTH_USERNAME", default="jobs4youmanager"
    )
    BASIC_AUTH_PASSWORD = os.environ.get("BASIC_AUTH_PASSWORD", default="admin")
    DEBUG = False
    IS_LOCAL = True if os.environ.get("IS_LOCAL", default=False) else False
    LOG_LEVEL = "INFO"
    PROPAGATE_EXCEPTIONS = False
    CACHE_TYPE = os.environ.get("CACHE_TYPE", "RedisCache")
    CACHE_DEFAULT_TIMEOUT = int(os.environ.get("CACHE_DEFAULT_TIMEOUT", 300))
    CACHE_KEY_PREFIX = os.environ.get("CACHE_KEY_PREFIX", "jobs4you_")
    CACHE_REDIS_URL = get_redis_conn_string()
    SQLALCHEMY_DATABASE_URI = get_psql_conn_string()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", default="RANDOM-SECRET-KEY-12345")
    TESTING = False
    VERSION = 0.1
