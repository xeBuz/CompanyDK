"""Added Owners

Revision ID: e377f177b029
Revises: 8db2fa0b4071
Create Date: 2016-03-20 16:16:20.522193

"""

from alembic import op
import sqlalchemy as sa
from api.models.owner import OwnerModel, CompanyModel


# revision identifiers, used by Alembic.
revision = 'e377f177b029'
down_revision = '8db2fa0b4071'


def upgrade():
    companies = CompanyModel.query.all()

    for company in companies:
        name = company.name + " Owner"
        owner = OwnerModel(name, company.id)
        owner.save()


def downgrade():
    pass
