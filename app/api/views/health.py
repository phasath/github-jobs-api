from datetime import datetime

from flask import current_app
from flask.views import MethodView

from app.api.serializers import HealthSerializer
from app.core.extensions import CONFIG

class HealthView(MethodView):
    
    schema = HealthSerializer()
    
    def liveness(self):
        response = {
            "name": current_app.name,
            "version": CONFIG.VERSION,
            "datetime": datetime.utcnow()
        }
        return self.schema.dump(response)