from flask_restful import request

def isAllowed(UserModel, session_creater):
    def outer(fun):
        def inner(*args, **kwargs):
            session = session_creater()
            user = session.query(UserModel).filter(token = request.headers.get("Authorization", None))
            fun(*args, **kwargs)
        return inner
    return outer