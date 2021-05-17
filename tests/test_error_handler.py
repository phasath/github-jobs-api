import pytest

from unittest import TestCase
from werkzeug.exceptions import BadRequest, RequestTimeout, BadGateway

from app.errors.error_handlers import generic_error_handler


@pytest.mark.parametrize(
    "error, expected",
    [
        (BadRequest("This is a Bad Request"), ({"error": {"title": "This is a Bad Request", "status": 400, "details": "()"}}, 400)),
        (RequestTimeout("Request has timed out"), ({"error": {"title": "Request has timed out", "status": 408, "details": "()"}}, 408)),
        (BadGateway("This is a Bad Gateway"), ({"error": {"title": "This is a Bad Gateway", "status": 502, "details": "()"}}, 502)),
     ]
)
def test_error_handler(app, error, expected):
    resp = generic_error_handler(error)

    TestCase().assertDictEqual(resp[0], expected[0])
    assert resp[1] == expected[1]