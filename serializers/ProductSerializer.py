from marshmallow import  Schema

class ProductSerializer(Schema):
    class Meta:
        fields = ('id', 'name')