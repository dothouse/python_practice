"""empty message

Revision ID: 836af5b573d5
Revises: 6d349dfc15a6
Create Date: 2024-01-18 18:27:09.037809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836af5b573d5'
down_revision = '6d349dfc15a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pension',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('day', sa.Float(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('reviewNum', sa.Float(), nullable=False),
    sa.Column('location', sa.String(length=200), nullable=False),
    sa.Column('pension_keyword', sa.String(length=200), nullable=False),
    sa.Column('addr', sa.String(length=200), nullable=False),
    sa.Column('ammen', sa.String(length=200), nullable=False),
    sa.Column('pensionID', sa.Float(), nullable=False),
    sa.Column('ammen1', sa.String(length=200), nullable=False),
    sa.Column('ammen2', sa.String(length=200), nullable=False),
    sa.Column('ammen3', sa.String(length=200), nullable=False),
    sa.Column('ammen4', sa.String(length=200), nullable=False),
    sa.Column('ammen5', sa.String(length=200), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pension')
    # ### end Alembic commands ###
