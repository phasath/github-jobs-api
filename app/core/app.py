import logging

import connexion

from connexion.resolver import MethodViewResolver

from app.core.config import Config
from app.core.extensions import CONFIG

logger = logging.getLogger(__name__)

def create_app(config: Config = CONFIG):
    application = connexion.FlaskApp("Jobs4You", specification_dir="app/openapi")

    application.app.config.from_object(config)

    application.add_api(
        "health.yml",
        base_path="/health",
        resolver=MethodViewResolver("app.api.health"),
        validate_responses=True,
        options={"swagger_ui": False},
    )
    
    return application.app

__all__ = ["create_app"]