import typing


from typing import Dict, Optional

from connexion import request
from flask.views import MethodView
from requests import status_codes

from app.api.serializers import JobsSerializer
from app.core.extensions import REQUESTS

from app.models import Search


class JobsView(MethodView):

    schema = JobsSerializer()

    def search(
        self,
        location: Optional[str] = None,
        language: Optional[str] = None,
        fulltime: bool = False,
    ) -> Dict:
        req_params = {
            "location": f'"{location}"' if location else None,
            "description": f'"{language}"' if language else None,
            "full_time": f"on" if fulltime else None,
            "utf8": "✓",
        }

        res = REQUESTS.get(f"https://jobs.github.com/positions.json", params=req_params)

        jobs = None

        if res.status_code == 200:
            jobs = res.json()

        search_data = {
            "location": location,
            "description": language,
            "full_time": fulltime,
            "ip_address": request.remote_addr,
        }

        search = Search(**search_data)
        search.save(commit=True)

        return self.schema.dump(jobs, many=True)
