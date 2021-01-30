"""empty message

Revision ID: d45e513b7836
Revises: 37b0522e7b6b
Create Date: 2021-01-30 18:58:24.707651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd45e513b7836'
down_revision = '37b0522e7b6b'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('case',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False, comment='用例ID'),
    sa.Column('SERIAL_NO', sa.String(length=128), nullable=False, comment='用例编号'),
    sa.Column('CREATE_TIME', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('UPDATE_TIME', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('DELETE_FLAG', sa.Boolean(), nullable=True, comment='删除标志'),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_case_SERIAL_NO'), 'case', ['SERIAL_NO'], unique=False)
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_case_SERIAL_NO'), table_name='case')
    op.drop_table('case')
    # ### end Alembic commands ###


def upgrade_extra():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_extra():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

