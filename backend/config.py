from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(application)