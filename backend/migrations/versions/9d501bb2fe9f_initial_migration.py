"""Initial migration.

Revision ID: 9d501bb2fe9f
Revises: a9305d1bbce7
Create Date: 2023-06-13 11:48:49.619118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d501bb2fe9f'
down_revision = 'a9305d1bbce7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pay', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mpesa_receipt_number', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('transaction_date', sa.DateTime(), nullable=False))
        batch_op.drop_constraint('pay_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pay', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('pay_user_id_fkey', 'users', ['user_id'], ['id'])
        batch_op.drop_column('transaction_date')
        batch_op.drop_column('mpesa_receipt_number')

    # ### end Alembic commands ###
