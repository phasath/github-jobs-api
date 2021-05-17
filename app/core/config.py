"""Configures the application
"""
import os


def get_conn_string():
    host = os.environ.get("PGHOST", "postgres")
    db = os.environ.get("PGDATABASE", "jobs4you")
    port = os.environ.get("PGPORT", "5432")
    username = os.environ.get("PGUSER", "jobs4you")
    password = os.environ.get("PGPASSWORD", "27613123j0b54You97402234")
    return f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"


class Config:
    APP_ENV = os.environ.get("APP_ENV", default="development")
    DEBUG = False
    IS_LOCAL = True if os.environ.get("IS_LOCAL", default=False) else False
    LOG_LEVEL = "INFO"
    PROPAGATE_EXCEPTIONS = False
    SQLALCHEMY_DATABASE_URI = get_conn_string()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", default="RANDOM-SECRET-KEY-12345")
    TESTING = False
    VERSION = 0.1
