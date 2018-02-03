import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_utils import Base

engine = create_engine('postgresql://{}:{}@{}:5432/{}'.format(
    os.environ['EMAILS_DB_USER'],
    os.environ['EMAILS_DB_PASSWORD'],
    os.environ['EMAILS_DB_HOST'],
    os.environ['EMAILS_DB_NAME']
), echo=True)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

from .EMailsModel import EMailsModel

__all__ = [
    'EMailsModel'
]

def crear_tablas():
    from .entities import Mail
    from sqlalchemy.schema import CreateSchema
    Base.metadata.create_all(engine)
