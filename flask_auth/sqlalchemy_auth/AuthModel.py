from sqlalchemy import Column, String, Boolean
from flask_auth.Utilities import PasswordManager

class Auth(PasswordManager):
    username = Column(String)
    password =  Column(String)
    salt =  Column(String)
    token =  Column(String)
    admin = Column(Boolean, default=0)
    staff = Column(Boolean, default=0)
    public = Column(Boolean, default=1)