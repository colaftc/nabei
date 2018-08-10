"""empty message

Revision ID: 37415d2a28f4
Revises: 
Create Date: 2018-08-01 04:07:02.536760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37415d2a28f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenditure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('price', sa.Numeric(precision=7, scale=2), nullable=True),
    sa.Column('pay_date', sa.Date(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outside_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('products', sa.Text(), nullable=True),
    sa.Column('total', sa.Numeric(precision=7, scale=2), nullable=True),
    sa.Column('order_date', sa.Date(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('urgent', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('outside_order')
    op.drop_table('expenditure')
    # ### end Alembic commands ###