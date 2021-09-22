"""empty message

Revision ID: ca14f127413e
Revises: f174e66938cb
Create Date: 2021-09-21 20:09:55.246793

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca14f127413e'
down_revision = 'f174e66938cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('people', 'favorites_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('planet', 'favorites_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('planet', 'favorites_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('people', 'favorites_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###