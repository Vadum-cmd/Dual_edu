"""Added es_word column into db_word table and changed user_id to id

Revision ID: eff6d8e90d72
Revises: 70fae727d58b
Create Date: 2023-04-10 21:15:18.219739

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'eff6d8e90d72'
down_revision = '70fae727d58b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('db_word', sa.Column('es_word', sa.String(length=90), nullable=False))
    
    op.drop_constraint('book_ibfk_1', 'book', type_='foreignkey')
    op.drop_constraint('user_word_ibfk_1', 'user_word', type_='foreignkey')
    op.drop_constraint('user_word_ibfk_2', 'user_word', type_='foreignkey')
    op.alter_column("user",
                     column_name = 'user_id',
                     primary_key=False
                     )
    op.alter_column("user",
                     column_name = 'user_id',
                     new_column_name = 'id',
                     existing_type = sa.Integer,
                     existing_nullable = False,
                     primary_key=True,
                     autoincrement=True
                    )
    op.create_foreign_key(
        'book_ibfk_1',
        'book',
        'user',
        ['user_id'],
        ['id'],
        ondelete='CASCADE'
    )
    op.create_foreign_key(
        'user_word_ibfk_1',
        'user_word',
        'book',
        ['book_id'],
        ['book_id'],
        ondelete='CASCADE'
    )
    op.create_foreign_key(
        'user_word_ibfk_2',
        'user_word',
        'db_word',
        ['en_word'],
        ['en_word'],
        ondelete='CASCADE'
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('db_word', 'es_word')
    # ### end Alembic commands ###
