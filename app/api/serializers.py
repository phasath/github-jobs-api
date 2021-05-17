from marshmallow import Schema
from marshmallow.fields import Bool, DateTime, Function, Int, Nested, Str, UUID


class HealthSerializer(Schema):
    name = Str(required=True)
    version = Str(required=True)
    datetime = DateTime(format="iso", required=True)


class JobsSerializer(Schema):
    company = Str(required=True)
    company_logo = Str(required=True)
    company_url = Str(required=True)
    created_at = Str(required=True)
    description = Str(required=True)
    fulltime = Bool(required=True)
    how_to_apply = Str(required=True)
    id = UUID(required=True)
    location = Str(required=True)
    title = Str(required=True)

    fulltime = Function(lambda obj: obj["type"] == "Full Time", data_key="fulltime")


class ErrorInternalSerializer(Schema):
    title = Str(required=True)
    status = Int(required=True)
    details = Str()


class ErrorSerializer(Schema):
    error = Nested(ErrorInternalSerializer)
