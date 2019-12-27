from flask_sqlalchemy import SQLAlchemy

db = None

def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:password@localhost/mysql'
