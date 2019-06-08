from flask_restful import request

def isAllowed(UserModel):
    def outer(fun):
        def inner(*args, **kwargs):
            user = UserModel.objects.filter(token = request.headers.get("Authorization", None))
            fun(*args, **kwargs)
        return inner
    return outer