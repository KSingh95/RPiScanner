#from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'c0d7a9a3401a772357254f4f9098bdaa'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1995@localhost:5000/rpidata'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
#db = SQLAlchemy(app)

from blogsite import routes
