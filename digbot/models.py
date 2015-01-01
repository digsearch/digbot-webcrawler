from sqlalchemy import create_engine, Column, BigInteger, String, Boolean, DateTime, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import settings


DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE), client_encoding='utf8')

def create_pages_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Page(DeclarativeBase):
    __tablename__ = "pages"

    id = Column(BigInteger, primary_key=True)
    url = Column('url', String, nullable=False)
    title = Column('title', String, nullable=False)
    content = Column('content', UnicodeText)
    last_crawled = Column('last_crawled', DateTime)
    spider = Column('spider', String)


class Domain(DeclarativeBase):
    __tablename__ = "domains"

    fqdn = Column('title', String, primary_key=True)
    ip_address = Column('ip_address', String, nullable=False)
    tasix_member = Column('tasix_member', Boolean, unique=False, default=False)
    last_crawled = Column('last_crawled', DateTime)
    spider = Column('spider', String)
