from mongoengine import StringField
from flask_auth.Utilities import PasswordManager

class Auth(PasswordManager):
    username = StringField()
    password = StringField()
    salt = StringField()
    token = StringField()

