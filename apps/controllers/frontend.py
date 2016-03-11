import datetime
from flask import Blueprint, render_template
from flask.views import MethodView

frontend = Blueprint('frontend', __name__)


class HealthController(MethodView):

    def get(self):
        """
        Returns a JSON with dummy data to test App
        """

        return render_template("index.html")


frontend_view = HealthController.as_view('frontend')
frontend.add_url_rule('', view_func=frontend_view, methods=['GET'])