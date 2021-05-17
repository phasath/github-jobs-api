import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def get_requests_session():
    ses = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    ses.mount("https://", HTTPAdapter(max_retries=retries))
    return ses
