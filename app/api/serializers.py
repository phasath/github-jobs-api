from marshmallow import Schema
from marshmallow.fields import Bool, DateTime, Function, Int, Nested, Str, UUID


class HealthSerializer(Schema):
    name = Str(required=True)
    version = Str(required=True)
    datetime = DateTime(format="iso", required=True)


class ErrorInternalSerializer(Schema):
    title = Str(required=True)
    status = Int(required=True)
    details = Str()

class ErrorSerializer(Schema):
    error = Nested(ErrorInternalSerializer)