import json

from unittest.mock import patch

from pytest import fixture

from app.core.extensions import CONFIG
from app.core import create_app


@fixture(scope="session")
def app(request):
    _app = create_app(CONFIG)

    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)

    with patch.multiple(
        CONFIG,
        DEBUG=True,
        TESTING=True,
    ):
        yield _app


@fixture(scope="session")
def parser():
    def _parser(res):
        return res.status_code, json.loads(res.data)

    yield _parser


@fixture(scope="session")
def client(app):
    with app.test_client() as client:
        yield client
