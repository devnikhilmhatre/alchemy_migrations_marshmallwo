from flask_restful import Resource, request
from db import start_session
from models.OrderModel import OrderModel

class OrderController(Resource):
    def get(self):
        return {}
    
    def post(self):
        # session = start_session()
        # order = OrderModel()
        return {}

    def put(self):
        return {}
    
    def delete(self):
        return {}