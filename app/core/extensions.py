from app.core.config import Config
from app.util.requests import get_requests_session

CONFIG = Config()
REQUESTS = get_requests_session()

__all__=["CONFIG", "REQUESTS"]