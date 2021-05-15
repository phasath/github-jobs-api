from marshmallow import Schema
from marshmallow.fields import Str, DateTime


class HealthSerializer(Schema):
    name = Str(required=True)
    version = Str(required=True)
    datetime = DateTime(format="iso", required=True)
