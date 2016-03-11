"""Added Country Field

Revision ID: 17d4c5d64a7b
Revises: 14cb7744656e
Create Date: 2016-03-10 21:48:47.654056

"""
from alembic import op
import sqlalchemy as sa

revision = '17d4c5d64a7b'
down_revision = '14cb7744656e'


def upgrade():
    op.add_column('co_company', sa.Column('country', sa.String(length=125), nullable=True))


def downgrade():
    op.drop_column('co_company', 'country')
