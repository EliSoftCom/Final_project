"""user, query, parsing, Result_parser tables

Revision ID: 5e259d620840
Revises: 
Create Date: 2024-07-21 22:10:36.331011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e259d620840'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Result_parser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Result_parser', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Result_parser_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_Result_parser_price'), ['price'], unique=False)
        batch_op.create_index(batch_op.f('ix_Result_parser_url'), ['url'], unique=True)

    op.create_table('parsing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_to_the_category', sa.String(), nullable=False),
    sa.Column('notification_email', sa.String(length=30), nullable=False),
    sa.Column('polling_interval', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('parsing', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_parsing_notification_email'), ['notification_email'], unique=False)
        batch_op.create_index(batch_op.f('ix_parsing_url_to_the_category'), ['url_to_the_category'], unique=True)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('query',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=256), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('query', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_query_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_query_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('query', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_query_user_id'))
        batch_op.drop_index(batch_op.f('ix_query_timestamp'))

    op.drop_table('query')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('parsing', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_parsing_url_to_the_category'))
        batch_op.drop_index(batch_op.f('ix_parsing_notification_email'))

    op.drop_table('parsing')
    with op.batch_alter_table('Result_parser', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Result_parser_url'))
        batch_op.drop_index(batch_op.f('ix_Result_parser_price'))
        batch_op.drop_index(batch_op.f('ix_Result_parser_name'))

    op.drop_table('Result_parser')
    # ### end Alembic commands ###
