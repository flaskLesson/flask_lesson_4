# https://lepture.com/en/2018/structure-of-a-flask-project
# 참고
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

user_bp = Blueprint("user", __name__)

db = SQLAlchemy(user_bp)

class User(db.Model):
    id = Column(db.Integer, nullable=False, primary_key=True)
    name = Column(db.String(255), nullable=False, default='')
    nick_name = Column(db.String(255), nullable=False, default='')
