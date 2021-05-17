import pytest

from unittest import TestCase
from datetime import datetime

from requests_mock import Mocker

from app.models import Search
from app.core.extensions import CONFIG

from tests.util.requests_mock_data import (
    get_fake_response,
    get_wrong_location,
    get_wrong_language,
)


@pytest.mark.parametrize(
    "location, language, fulltime, expected, status_code",
    [
        (None, None, False, get_fake_response, 200),
        ("san francisco", None, False, get_fake_response, 200),
        ("san francisco", "python", False, get_fake_response, 200),
        ("beijing", "python", True, get_fake_response, 200),
        ("san frasciso", "python", False, get_wrong_location, 400),
        ("san francisco", "pythona", False, get_wrong_language, 400),
    ],
)
def test_get_jobs(
    client, db, parser, location, language, fulltime, expected, status_code
):
    with Mocker() as m:
        m.get("https://jobs.github.com/positions.json", json=expected)

        r_location = f"location={location}" if location else ""
        r_language = f"language={language}" if language else ""
        r_fulltime = f"fulltime={fulltime}" if fulltime else ""

        res = client.get(
            f"/jobs?{r_location}&{r_language}&{r_fulltime}",
        )

        st_code, response = parser(res)
        assert st_code == status_code
        assert len(response) == len(expected)

        if st_code == 200:
            q_location = f'"{location}"' if location else None
            q_language = f'"{language}"' if language else None

            db_data = (
                Search.query.filter(
                    Search.location == q_location,
                    Search.description == q_language,
                    Search.full_time == fulltime,
                )
                .order_by(Search.time.desc())
                .limit(1)
                .one()
            )

            TestCase().assertTrue(db_data)
