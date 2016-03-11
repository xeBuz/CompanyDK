"""Added Companies

Revision ID: 2e16030bde45
Revises: 14cb7744656e
Create Date: 2016-03-10 21:33:14.544867

"""
# from alembic import op
# import sqlalchemy as sa
from apps.models.company import CompanyModel


revision = '2e16030bde45'
down_revision = '14cb7744656e'


def upgrade():
    microsoft = CompanyModel("Microsoft", "Random Address", "Redmond", "USA", "contact@mns.com", "1-800-642-7676")
    microsoft.save()

    oracle = CompanyModel("Oracle", "Random Oracle Address", "Redwood City", "USA", "info@oracle.com", "00 1 650-506-7000")
    oracle.save()

    sap = CompanyModel("SAP", "Address 123 - Floor 4th", "Walldorf", "Germany", "info@sap.com", "+1-800-872-1727")
    sap.save()

    amazon = CompanyModel("Amazon", "No Address", "Seattle", "USA", "contact@amazon.com", "00 1 206-266-2992")
    amazon.save()

    google = CompanyModel("Google", "Try Google Maps 143", "Mountain View", "USA", "hello@google.com", "1-866-246-6453")
    google.save()

    skynet = CompanyModel("SkyNet", "N/A", "California", "USA", "bot@skynet.com")
    skynet.save()

    dharma = CompanyModel("Dharma Initiative", "N/A", "Michigan", "USA", "research@dharma-initiative.org")
    dharma.save()

    wayne = CompanyModel("Wayne Enterprises", "Wayne Tower", "Gotham City", "USA", "bruce@wayne.com")
    wayne.save()

    robotics = CompanyModel("U.S. Robotics and Mechanical Men", "N/A", "New York", "USA", "susan.calvin@robotics.com", "555 5555 555")
    robotics.save()

    tyler = CompanyModel("Tyrell Corporation", "N/A", "Los Angeles", "USA", "douglastrumbull@tyrell.com", "N/A")
    tyler.save()

    ocp = CompanyModel("Omni Consumer Products", "N/A", "Detroit", "USA", "ed209@ocp.net")
    ocp.save()

    ingen = CompanyModel("INGen", "Palo Alto", "California", "USA", "wemakefuture@ingen.com")
    ingen.save()


def downgrade():
    pass

