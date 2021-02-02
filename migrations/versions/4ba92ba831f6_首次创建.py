"""‘首次创建’

Revision ID: 4ba92ba831f6
Revises: 
Create Date: 2021-02-02 21:26:15.502964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ba92ba831f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('case',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('CREATE_TIME', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('UPDATE_TIME', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('DELETE_FLAG', sa.Boolean(), nullable=True, comment='删除标志'),
    sa.Column('SERIAL_NO', sa.String(length=128), nullable=False, comment='用例编号'),
    sa.Column('LEVEL', sa.String(length=1), nullable=False, comment='用例等级'),
    sa.Column('DESCRIPTION', sa.String(length=32), nullable=False, comment='用例描述'),
    sa.Column('REQUEST_METHOD', sa.Enum('GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'), nullable=False, comment='请求方法'),
    sa.Column('REQUEST_HEADERS', sa.JSON(), nullable=True, comment='请求头'),
    sa.Column('REQUEST_BODY', sa.JSON(), nullable=True, comment='请求体'),
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
    op.create_table('user',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('CREATE_TIME', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('UPDATE_TIME', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('DELETE_FLAG', sa.Boolean(), nullable=True, comment='删除标志'),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('confirm_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade_extra():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

