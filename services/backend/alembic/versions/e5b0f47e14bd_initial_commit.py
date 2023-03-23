"""Initial commit

Revision ID: e5b0f47e14bd
Revises: 
Create Date: 2023-03-18 14:11:04.119416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5b0f47e14bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('db_word',
    sa.Column('en_word', sa.String(length=50), nullable=False),
    sa.Column('word_level', sa.String(length=2), nullable=False),
    sa.Column('uk_word', sa.String(length=90), nullable=False),
    sa.PrimaryKeyConstraint('en_word')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('current_num_level', sa.Integer(), nullable=False),
    sa.Column('goal_level', sa.String(length=2), nullable=False),
    sa.Column('user_level', sa.String(length=3), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('native_language', sa.String(length=50), nullable=False),
    sa.Column('frame_path', sa.String(length=120), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('book',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('book_title', sa.String(length=50), nullable=False),
    sa.Column('book_author', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('user_word',
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('en_word', sa.String(length=50), nullable=False),
    sa.Column('is_known', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], ),
    sa.ForeignKeyConstraint(['en_word'], ['db_word.en_word'], ),
    sa.PrimaryKeyConstraint('word_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_word')
    op.drop_table('book')
    op.drop_table('user')
    op.drop_table('db_word')
    # ### end Alembic commands ###
