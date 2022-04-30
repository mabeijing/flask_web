from datetime import datetime
import json
from typing import Literal

from sqlalchemy import Integer, Column, String, Enum, JSON
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from db_orm import Model

engine = create_engine('postgresql+psycopg2://postgres:root123@localhost:5432/dbname', echo=False)
session = scoped_session(session_factory=sessionmaker(bind=engine))
METHOD = Literal["POST", "GET", "PUT", "UPDATE", "DELETE"]


class TBUser(Model):
    __tablename__ = 'tb_user'

    def __init__(self, user_id: int = None, user_name: str = None):
        self.USER_ID = user_id
        self.USERNAME = user_name

    USER_ID = Column(Integer, nullable=False, unique=True, index=True, comment='用户ID')
    USERNAME = Column(String(30), nullable=False, comment='用户名')
    PASSWORD = Column(String(50), comment='密码')

    def save(self):
        session.add(self)
        session.commit()

    def update(self):
        self.UPDATE_TIME = datetime.now()
        session.commit()

    @property
    def filter(self):
        return session.query(self.__class__).filter

    def delete(self):
        session.delete(self)
        session.commit()

    def check_exist(self):
        return session.query(self.__class__).filter_by(USER_ID=self.USER_ID).first()

    def query(self):
        return session.query(self.__class__).filter_by(USER_ID=self.USER_ID).first()

    def __repr__(self):
        return f'{self.__class__.__name__}(ID={self.ID},USER_ID={self.USER_ID}, USERNAME={self.USERNAME}, DELETE={self.IS_DELETE})'

    def to_dict(self):
        return {
            'user_id': self.USER_ID,
            'user_name': self.USERNAME
        }

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)


class TBRequest(Model):
    __tablename__ = 'tb_request'

    def __init__(self, name: str = None, description: str = None, url: str = None, method: METHOD = None,
                 headers: dict = None, content_type: dict = None,
                 body: dict = None, auth: str = None):
        self.NAME = name
        self.DESC = description
        self.URL = url
        self.METHOD = method
        self.HEADERS = headers
        self.CONTENT_TYPE = content_type
        self.BODY = body
        self.AUTH = auth

    NAME = Column(String(50), nullable=False, unique=True, index=True, comment='请求名字')
    DESC = Column(String(100), comment='描述信息')
    URL = Column(String(100), nullable=False, comment='请求url')
    METHOD = Column(Enum('POST', 'GET', 'PUT', 'DELETE', name='METHOD'), nullable=False, comment='请求方法')
    HEADERS = Column(JSON, comment='请求头')
    CONTENT_TYPE = Column(JSON, comment='请求体类型')
    BODY = Column(JSON, comment='请求体')
    AUTH = Column(String(200), comment='认证')

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def query(cls, name: str):
        return session.query(cls).filter_by(NAME=name).first()

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.NAME},desc={self.DESC}, url={self.URL}, method={self.METHOD}, headers={self.HEADERS}, body={self.BODY})'


if __name__ == '__main__':
    Model.metadata.create_all(engine, checkfirst=True)
