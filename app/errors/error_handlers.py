from app.api.serializers import ErrorSerializer


def generic_error_handler(error):
    payload = {
        "error": {
            "title": error.description,
            "status": error.code,
            "details": str(error.args),
        }
    }

    return ErrorSerializer().dump(payload), error.code
