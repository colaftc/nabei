"""empty message

Revision ID: f3bfd58659f9
Revises: 3b60ab5fe035
Create Date: 2018-07-17 06:16:19.606301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3bfd58659f9'
down_revision = '3b60ab5fe035'
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('outside_order')
    op.drop_table('expenditure')
    # ### end Alembic commands ###