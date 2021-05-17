import typing


from typing import Dict

from flask.views import MethodView
from requests import status_codes

from app.api.serializers import JobsSerializer
from app.core.extensions import REQUESTS


class JobsView(MethodView):
    
    schema = JobsSerializer()
    
    def search(self, location: str = "", language: str = "", fulltime: bool = False) -> Dict:
        params = {
            "location": f'"{location}"' if location else "",
            "language": f'"{language}"' if language else "",
            "full_time": f'on' if fulltime else "",
            "utf8": "✓",
        }

        res = REQUESTS.get(
            f'https://jobs.github.com/positions.json',
            params=params
        )
        
        jobs = None
        if res.status_code == 200:
            jobs = res.json()

       
        return self.schema.dump(jobs, many=True)