"""empty message

Revision ID: 99aa3c0208af
Revises: fefca8ddc81d
Create Date: 2018-07-17 05:48:03.571040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99aa3c0208af'
down_revision = 'fefca8ddc81d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('outside_order', sa.Column('pay_date', sa.Date(), nullable=True))
    op.add_column('outside_order', sa.Column('price', sa.Numeric(), nullable=True))
    op.add_column('outside_order', sa.Column('title', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('outside_order', 'title')
    op.drop_column('outside_order', 'price')
    op.drop_column('outside_order', 'pay_date')
    # ### end Alembic commands ###
