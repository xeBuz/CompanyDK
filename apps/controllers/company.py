from flask import Blueprint, request
from flask.views import MethodView
from apps.controllers.base import BaseController
from apps.models.company import CompanyModel

companies = Blueprint('companies', __name__)


class CompanyController(MethodView, BaseController):

    def get(self, company_id):
        """
        Returns in JSON format one or many Companies

        :param company_id:
        """
        if company_id is not None:
            """ lalala """
            return self.response(200, company_id)

        else:
            """ lalala """
            return self.response(200)

    def post(self):
        """
        Create a new Company

        :return: Code 201
        """
        return self.response(201)

    def put(self, company_id):
        """
        Edit a Company

        :param company_id:
        :return: Code 200
        """
        return self.response(202)

    def delete(self, company_id):
        """
        Delete a Company

        :param company_id:
        :return:
        """
        return self.response(204)


companies_view = CompanyController.as_view('companies')
companies.add_url_rule('', view_func=companies_view, methods=['POST'])
companies.add_url_rule('', defaults={'company_id': None}, view_func=companies_view, methods=['GET'])
companies.add_url_rule('/<int:company_id>', view_func=companies_view, methods=['GET', 'PUT', 'DELETE'])