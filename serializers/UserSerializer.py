from marshmallow import Schema, fields
from serializers.OrderSerializer import OrderSerializer

class UserSerializer(Schema):
    orders = fields.Nested(OrderSerializer, many=True)
    class Meta:
        fields = ('id', 'name', 'age' ,'orders', 'username')
