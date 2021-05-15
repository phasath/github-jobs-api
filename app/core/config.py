"""Configures the application
"""
import os


class Config:
    APP_ENV = os.environ.get("APP_ENV", default="development")
    VERSION = 0.1
    LOG_LEVEL = "INFO"
    SECRET_KEY = os.environ.get("SECRET_KEY", default="RANDOM-SECRET-KEY-12345")