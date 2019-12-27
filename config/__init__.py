from flask import Flask



class initClass() :
    def __init__(self):
        # import routes
        # import services
        # import models
        self.app = Flask(__name__)

        self.app.config['SECRET_KEY'] = 'this is secret'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:acriil4958@localhost:3306/study_db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    def get_app(self):
        return self.app