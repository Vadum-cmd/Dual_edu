"""Added word_type column in DB_word table

Revision ID: 70fae727d58b
Revises: e5b0f47e14bd
Create Date: 2023-03-20 21:48:57.561735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70fae727d58b'
down_revision = 'e5b0f47e14bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('db_word', sa.Column('word_type', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('db_word', 'word_type')
    # ### end Alembic commands ###
