"""Added Table: Company

Revision ID: 14cb7744656e
Revises: None
Create Date: 2016-03-10 21:25:07.056290

"""
from alembic import op
import sqlalchemy as sa

revision = '14cb7744656e'
down_revision = None


def upgrade():
    op.create_table('co_company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=125), nullable=True),
    sa.Column('address', sa.String(length=125), nullable=True),
    sa.Column('city', sa.String(length=125), nullable=True),
    sa.Column('email', sa.String(length=125), nullable=True),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('co_company')
