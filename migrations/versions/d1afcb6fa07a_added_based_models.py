"""added based models

Revision ID: d1afcb6fa07a
Revises: 
Create Date: 2022-01-22 18:46:09.367140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1afcb6fa07a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=True),
    sa.Column('roles', sa.String(length=12), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tamagochi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('sleep', sa.Float(), nullable=True),
    sa.Column('food', sa.Float(), nullable=True),
    sa.Column('game', sa.Float(), nullable=True),
    sa.Column('health', sa.Float(), nullable=True),
    sa.Column('general_state', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tamagochi')
    op.drop_table('user')
    # ### end Alembic commands ###
