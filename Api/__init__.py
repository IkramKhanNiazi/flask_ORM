import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql6418048:C9CTgh9qdV@sql6.freemysqlhosting.net/sql6418048'

from Api import models
from Api import views
