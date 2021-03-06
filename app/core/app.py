import logging

import connexion

from connexion.resolver import MethodViewResolver
from flask import Flask
from werkzeug.exceptions import default_exceptions

from app.core.admin import admin_setup
from app.core.config import Config
from app.core.extensions import CACHE, CONFIG, DB
from app.errors.error_handlers import generic_error_handler

logger = logging.getLogger(__name__)


def create_app(config: Config = CONFIG) -> Flask:
    application = connexion.FlaskApp("Jobs4You", specification_dir="app/openapi")

    application.app.config.from_object(config)

    application.add_api(
        "health.yml",
        base_path="/api/health",
        resolver=MethodViewResolver("app.api"),
        validate_responses=True,
        options={"swagger_ui": False},
    )

    application.add_api(
        "jobs.yml",
        base_path="/api",
        resolver=MethodViewResolver("app.api"),
        validate_responses=True,
        options={"swagger_ui": True},
    )

    for exc in default_exceptions:
        application.app.register_error_handler(exc, generic_error_handler)

    DB.init_app(application.app)

    CACHE.init_app(application.app)

    admin_setup(application.app)

    return application.app


__all__ = ["create_app"]
