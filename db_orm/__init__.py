from sqlalchemy import Column
from sqlalchemy import DateTime, Boolean, Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Model(Base):
    __abstract__ = True
    ID = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    CREATE_TIME = Column(DateTime, default=datetime.now, comment='创建时间')
    UPDATE_TIME = Column(DateTime, default=None, comment='更新时间')
    DELETE_TIME = Column(DateTime, default=None, comment='删除时间')
    IS_DELETE = Column(Boolean, default=False, comment='逻辑删除')
