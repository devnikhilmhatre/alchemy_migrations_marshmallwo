from sqlalchemy import Column, Integer, String

from db import Base


class ProductModel(Base):
    __tablename__ = 'product'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
