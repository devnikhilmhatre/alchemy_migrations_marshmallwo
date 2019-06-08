from flask import Flask
from flask_restful import Api

from controllers.OrderController import OrderController
from controllers.UserController import UserController
from controllers.ProductController import ProductController


app = Flask(__name__)
route = Api(app)

# All routes
route.add_resource(UserController, '/users', '/user/<int:id>')
route.add_resource(ProductController, '/products')
route.add_resource(OrderController, '/orders')

if __name__ == "__main__":
    app.run(debug=True)
