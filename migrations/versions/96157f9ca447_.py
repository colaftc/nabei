"""empty message

Revision ID: 96157f9ca447
Revises: 
Create Date: 2018-02-19 23:47:09.090780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96157f9ca447'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('outside_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('products', sa.Text(), nullable=True),
    sa.Column('total', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('outside_order')
    # ### end Alembic commands ###
