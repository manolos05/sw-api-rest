"""empty message

Revision ID: 09f0247d0b6b
Revises: 4279cbd56d2e
Create Date: 2023-06-06 01:29:17.945471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09f0247d0b6b'
down_revision = '4279cbd56d2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fav__planet',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.planet_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'planet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav__planet')
    # ### end Alembic commands ###
