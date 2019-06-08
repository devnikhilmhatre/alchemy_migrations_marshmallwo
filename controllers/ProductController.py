from flask_restful import Resource, request

from db import start_session
from models.ProductModel import ProductModel
from serializers.ProductSerializer import ProductSerializer


class ProductController(Resource):
    def get(self):
        session = start_session()
        products = session.query(ProductModel).all()
        serializer = ProductSerializer(many=True)
        serializer = serializer.dump(products)
        return serializer.data
    
    def post(self):
        session = start_session()
        product = ProductModel(**request.json)
        session.add(product)
        session.commit()

        serializer = ProductSerializer()
        serializer = serializer.dump(product)
        return serializer.data
    
    def put(self):
        return {}
    
    def delete(self):
        return {}
