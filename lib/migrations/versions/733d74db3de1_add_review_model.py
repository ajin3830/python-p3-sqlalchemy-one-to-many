"""Add Review Model

Revision ID: 733d74db3de1
Revises: 9f74f06cf678
Create Date: 2023-03-09 21:15:55.979332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '733d74db3de1'
down_revision = '9f74f06cf678'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
