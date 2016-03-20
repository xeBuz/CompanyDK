"""Added Company's Owners

Revision ID: 8db2fa0b4071
Revises: 2e16030bde45
Create Date: 2016-03-20 16:04:44.169101

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8db2fa0b4071'
down_revision = '2e16030bde45'


def upgrade():
    op.create_table('co_owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=125), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], [u'co_company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('co_owner')
