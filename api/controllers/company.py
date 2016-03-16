from flask import Blueprint, request
from flask.views import MethodView
from api.controllers.base import BaseController
from api.models.company import CompanyModel

companies = Blueprint('companies', __name__)


class CompanyController(MethodView, BaseController):

    def get(self, company_id):
        """
        Returns in JSON format one or many Companies

        :param company_id:
        """
        pagination = None

        if company_id is None:
            page = int(request.args.get('page', '1'))
            count = int(request.args.get('count', '5'))

            pagination = CompanyModel.query.paginate(page, count, False)
            company = pagination.items

            if len(company) == 0:
                return self.response(404)

        else:
            company = CompanyModel.query.filter_by(id=company_id).first()
            if company is None:
                return self.response(404)

        return self.response(200, company, pagination)

    def post(self):
        """
        Create a new Company

        :return: Code 201
        """

        name = request.form.get('name')
        address = request.form.get('address')
        city = request.form.get('city')
        country = request.form.get('country')
        email = request.form.get('email')
        phone = request.form.get('phone')

        if name is None or address is None or city is None or country is None:
            self.response(400)

        company = CompanyModel(
            name=name,
            address=address,
            city=city,
            country=country,
            email=email,
            phone=phone
        )

        company.save()
        return self.response(201, {'id': company.id})

    def put(self, company_id):
        """
        Edit a Company

        :param company_id:
        :return: Code 200
        """

        if company_id is None:
            return self.response(400)

        company = CompanyModel.query.filter_by(id=company_id).first()
        if company is None:
            return self.response(404)

        name = request.form.get('name')
        if name:
            company.name = name

        address = request.form.get('address')
        if address:
            company.address = address

        city = request.form.get('city')
        if city:
            company.city = city

        country = request.form.get('country')
        if country:
            company.country = country

        email = request.form.get('email')
        if email:
            company.email = email

        phone = request.form.get('phone')
        if phone:
            company.phone = phone

        company.save()
        return self.response(200)

    def delete(self, company_id):
        """
        Delete a Company

        :param company_id:
        :return:
        """

        if company_id is None:
            return self.response(400)

        company = CompanyModel.query.filter_by(id=company_id).first()
        if company is None:
            return self.response(404)

        company.delete()
        return self.response(200)

companies_view = CompanyController.as_view('companies')
companies.add_url_rule('', view_func=companies_view, methods=['POST'])
companies.add_url_rule('', defaults={'company_id': None}, view_func=companies_view, methods=['GET'])
companies.add_url_rule('/<int:company_id>', view_func=companies_view, methods=['GET', 'PUT', 'DELETE'])