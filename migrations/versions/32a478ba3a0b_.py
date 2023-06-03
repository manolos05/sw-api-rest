"""empty message

Revision ID: 32a478ba3a0b
Revises: 561ab3204cb8
Create Date: 2023-06-02 23:07:51.186833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32a478ba3a0b'
down_revision = '561ab3204cb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('population', sa.String(length=80), nullable=False),
    sa.Column('climate', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('planet_id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###