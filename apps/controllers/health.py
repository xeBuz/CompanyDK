import datetime
from flask import Blueprint
from flask.views import MethodView
from apps.controllers.base import BaseController


health = Blueprint('health', __name__)


class HealthController(MethodView, BaseController):

    def get(self):
        """
        Returns a JSON with dummy data to test App
        """

        json_response = {
            'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        return self.response(200, json_response)


health_view = HealthController.as_view('health')
health.add_url_rule('', view_func=health_view, methods=['GET'])