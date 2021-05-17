"""Configures the application
"""
import os


class Config:
    APP_ENV = os.environ.get("APP_ENV", default="development")
    DEBUG = False
    LOG_LEVEL = "INFO"
    PROPAGATE_EXCEPTIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", default="RANDOM-SECRET-KEY-12345")
    TESTING = False
    VERSION = 0.1