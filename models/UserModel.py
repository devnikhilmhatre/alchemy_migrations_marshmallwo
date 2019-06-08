from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base
from flask_auth.sqlalchemy_auth.AuthModel import Auth

class UserModel(Base, Auth):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    orders = relationship('OrderModel', back_populates='user')
