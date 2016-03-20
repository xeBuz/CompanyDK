from flask import Blueprint, request
from flask.views import MethodView
from api.controllers.base import BaseController
from api.models.company import CompanyModel
from api.models.owner import OwnerModel

owners = Blueprint('owners', __name__)


class OwnerController(MethodView, BaseController):

    def get(self, owner_id, company_id):
        """
        Returns in JSON format one or many Companies

        :param owner_id:
        :param company_id:
        """
        pagination = None
        owners = None

        if company_id is None and owner_id is None:
            page = int(request.args.get('page', '1'))
            count = int(request.args.get('count', '5'))

            pagination = OwnerModel.query.paginate(page, count, False)
            owners = pagination.items

            if len(owners) == 0:
                return self.response(404)

        elif company_id:
            page = int(request.args.get('page', '1'))
            count = int(request.args.get('count', '5'))

            pagination = OwnerModel.query.filter_by(company_id=company_id).paginate(page, count, False)
            owners = pagination.items

            if len(owners) == 0:
                return self.response(404)

        elif owner_id:
            owners = OwnerModel.query.filter_by(id=owner_id).first()
            if owners is None:
                return self.response(404)

        return self.response(200, owners, pagination)

    def post(self):
        """
        Create a new Owner

        :return: Code 201
        """

        name = request.form.get('name')
        company_id = request.form.get('company_id')

        company = CompanyModel.query.filter_by(id=company_id).first()
        if company is None or name is None:
            return self.response(400)

        owner = OwnerModel(
            name=name,
            company_id=company_id
        )

        owner.save()
        return self.response(201, {'id': owner.id})

    def put(self, owner_id):
        """
        Edit a Owner

        :param owner_id:
        :return: Code 200
        """

        if owner_id is None:
            return self.response(400)

        owner = OwnerModel.query.filter_by(id=owner_id).first()
        if owner is None:
            return self.response(404)

        name = request.form.get('name')
        if name:
            owner.name = name

        company_id = request.form.get('company_id')
        if company_id:
            company = CompanyModel.query.filter_by(id=company_id).first()
            if company is None:
                return self.response(404)

            owner.address = company_id

        owner.save()
        return self.response(200)

    def delete(self, owner_id):
        """
        Delete a Owner

        :param owner_id:
        :return:
        """

        if owner_id is None:
            return self.response(400)

        owner = OwnerModel.query.filter_by(id=owner_id).first()
        if owner is None:
            return self.response(404)

        owner.delete()
        return self.response(200)

owners_view = OwnerController.as_view('owners')
owners.add_url_rule('', view_func=owners_view, methods=['POST'])
owners.add_url_rule('/', defaults={'owner_id': None, 'company_id': None}, view_func=owners_view, methods=['GET'])
owners.add_url_rule('/company/<int:company_id>', defaults={'owner_id': None}, view_func=owners_view, methods=['GET'])
owners.add_url_rule('/<int:owner_id>/', defaults={'company_id': None}, view_func=owners_view, methods=['GET', 'PUT', 'DELETE'])
