from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class OrderModel(Base):
    __tablename__ = 'order'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    # product_id = Column(Integer, ForeignKey('product.id'))

    user = relationship('UserModel', back_populates='orders')
    # product = relationship('ProductModel', back_populates='orders')
