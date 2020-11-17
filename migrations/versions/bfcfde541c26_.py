"""empty message

Revision ID: bfcfde541c26
Revises: 
Create Date: 2020-11-10 14:11:36.962374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfcfde541c26'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=120), nullable=False),
    sa.Column('done', sa.Boolean(create_constraint=False), nullable=False),
    sa.Column('user_to_do', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['user_to_do'], ['user.user_name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('user')
    # ### end Alembic commands ###