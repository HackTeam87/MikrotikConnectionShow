# -*- coding: utf-8 -*-
import os
db_login = os.getenv('DB_ROUTERS_LOGIN', default=None)
db_passwd = os.getenv('DB_ROUTERS_PASSWD', default=None)
#printenv | more
#/etc/environment
#DB_ROUTERS_LOGIN=''
#DB_ROUTERS_PASSWD=''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_login}:{db_passwd}@localhost/routers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)
# from databse.models import *





