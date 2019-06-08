from flask_restful import Resource, request
from sqlalchemy import func, and_, or_ # func sql functions
from sqlalchemy.orm import selectinload, joinedload, contains_eager

from db import start_session
from models.UserModel import UserModel
from models.OrderModel import OrderModel
from serializers.UserSerializer import UserSerializer

# import copy


class UserController(Resource):
    def get(self):
        # request.args --> query string params as dict
        session = start_session()

        # name = request.args['name']
        
        # load all rows (select *)
        users = session.query(UserModel)



        # left outer join eager load --> 2nd option
        # users = users.outerjoin(OrderModel).options(contains_eager(UserModel.orders))

        # left outer join eager load --> 1st option
        # users = users.options(joinedload(UserModel.orders))

        # 2nd query --> select in query
        # users = users.options(selectinload(UserModel.orders))

        # left outer join
        # users = users.outerjoin(UserModel.orders)
        
        # for user in users:
        #     print(user.orders)

        # search query --> case insensitive with ilike and case sensitive with like
        # users = users.filter(UserModel.name.ilike('%{}%'.format(name)))

        
        # many=True for list of objects

        serializer = UserSerializer(many=True)
        serializer = serializer.dump(users)
        return serializer.data
    
    def post(self):
        # comment 1
        # request.json --> json data --> application/json
        # request.files --> uploaded files (form-data)
        # request.form --> form-data

        session = start_session()
        password = request.json.pop('password')
        user = UserModel(**request.json)
        user.set_password(password)
        session.add(user)
        
        # comment 2
        # session.flush()
        # adds the data in db, 
        # but if "rollback" is called 
        # or no "commit" performed 
        # all data is removed (auto increment pk increases with flush)
        
        # comment 3
        # using flush and making deepcopy
        # can save a db hit (i.e. select called after session expires)
        # user = copy.deepcopy(user)
        
        session.commit()
        
        # comment 4
        # after commit all session expires.
        # so accessing "user" object again will make another db query 
        # (this db hit can be avoided by using *commnet 3*)
        
        # comment 5
        # with the help of serializer
        # we're converting python object to dict 
        serializer = UserSerializer()
        data = serializer.dump(user)
        
        return data.data
    
    def put(self, id):
        # start the session
        session = start_session()
        
        # Update without select (1 query)
        # session.query(UserModel).filter(id==id).update({
        #     "name" : "Nikhil M"
        # }, synchronize_session = False)
        
        # Update with select (2 queries)
        # user = session.query(UserModel).get(id)
        # user.name = 'Nikhil'

        session.commit()
        
        serializer = UserSerializer()
        data = serializer.dump(user)
        return data.data

    def delete(self):
        # start the session
        session = start_session()

        # make a query
        session.query(UserModel).delete()

        # commit the changes
        session.commit()
        return {}