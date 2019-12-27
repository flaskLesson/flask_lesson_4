from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:acriil4958@localhost:3306/study_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    uid = Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    password = Column(db.String(100), nullable=False)
    first_name = Column(db.String(100), nullable=False)
    last_name = Column(db.String(100), nullable=False)
    email = Column(db.String(100), nullable=True)
    gender = Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User('{self.uid}', '{self.first_name}', '{self.email}')>"


class Test(db.Model):
    __tablename__ = 'test'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(db.String(100), nullable=True, primary_key=True)
    tttt = Column(db.String(100), nullable=True)


db.create_all()


@app.route('/')
@app.route('/login')
def index():
    return render_template('user/login.html')


@app.route("/user/login", methods=["POST"])
def login():
    if request.method == 'POST':
        req = request.form

        # 데이터 받기
        email = req.get("email")
        pw = req.get("password")

        # 서버 연결
        rowCount = User.query.filter_by(email=email, password=pw).count()
        row = None
        if rowCount == 0:
            row = User.query.all()
        else:
            row = User.query.filter_by(email=email, password=pw)

        return render_template('user/show.html', row=row)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050', debug=True)
