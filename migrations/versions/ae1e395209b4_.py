"""empty message

Revision ID: ae1e395209b4
Revises: ca14f127413e
Create Date: 2021-09-22 15:49:15.647862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae1e395209b4'
down_revision = 'ca14f127413e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('favorite_id', sa.Integer(), nullable=False))
    op.add_column('favorites', sa.Column('tipo', sa.String(length=40), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('favorites', 'tipo')
    op.drop_column('favorites', 'favorite_id')
    # ### end Alembic commands ###
