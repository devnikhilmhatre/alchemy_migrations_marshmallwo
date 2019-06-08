from marshmallow import Schema

class OrderSerializer(Schema):
    class Meta:
        fields = ('id', 'user_id', 'product_id')

    # user = relationship('UserModel', back_populates='orders')
    # product = relationship('ProductModel', back_populates='orders')
