from os import environ

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

Base = declarative_base()

# with echo=True logs out all sql queries in terminal
engine = create_engine(environ.get('db_url'), echo=True)
# engine = create_engine(environ.get('db_url'))

start_session = sessionmaker(bind=engine)
