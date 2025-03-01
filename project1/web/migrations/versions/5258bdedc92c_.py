"""empty message

Revision ID: 5258bdedc92c
Revises: e40797f6c099
Create Date: 2024-01-19 12:23:21.329179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5258bdedc92c'
down_revision = 'e40797f6c099'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pensionID', sa.String(length=200), nullable=False))
        batch_op.create_foreign_key(None, 'pension', ['pensionID'], ['pensionID'])
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.FLOAT(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('pensionID')

    # ### end Alembic commands ###
