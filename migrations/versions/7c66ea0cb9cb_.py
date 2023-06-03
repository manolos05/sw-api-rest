"""empty message

Revision ID: 7c66ea0cb9cb
Revises: ce10296491ba
Create Date: 2023-06-03 02:05:57.510727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c66ea0cb9cb'
down_revision = 'ce10296491ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_column('color_eyes')
        batch_op.drop_column('height')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('height', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('color_eyes', sa.VARCHAR(length=80), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
