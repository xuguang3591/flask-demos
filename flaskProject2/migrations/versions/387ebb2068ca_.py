"""empty message

Revision ID: 387ebb2068ca
Revises: 7259c79c738b
Create Date: 2022-04-09 08:17:02.225949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '387ebb2068ca'
down_revision = '7259c79c738b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('food', sa.String(length=30), nullable=True),
    sa.Column('flag', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cats')
    # ### end Alembic commands ###
