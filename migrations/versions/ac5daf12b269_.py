"""empty message

Revision ID: ac5daf12b269
Revises: d8f6874be209
Create Date: 2021-09-22 20:51:34.234931

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ac5daf12b269'
down_revision = 'd8f6874be209'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('people_ibfk_1', 'people', type_='foreignkey')
    op.drop_column('people', 'favorites_id')
    op.drop_constraint('planet_ibfk_1', 'planet', type_='foreignkey')
    op.drop_column('planet', 'favorites_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('favorites_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('planet_ibfk_1', 'planet', 'favorites', ['favorites_id'], ['id'], ondelete='CASCADE')
    op.add_column('people', sa.Column('favorites_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('people_ibfk_1', 'people', 'favorites', ['favorites_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###