from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
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
    email = Column(db.String(100), nullable=False)
    password = Column(db.String(100), nullable=False)
    first_name = Column(db.String(100), nullable=True)
    last_name = Column(db.String(100), nullable=True)
    gender = Column(db.String(100), nullable=False)

    def __init__(self, email, password, gender, first_name=None, last_name=None):
        self.email = email
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def __repr__(self):
        return f"<User('{self.uid}', '{self.first_name}', '{self.email}')>"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Test(db.Model):
    __tablename__ = 'test'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(db.String(100), nullable=True, primary_key=True)
    tttt = Column(db.String(100), nullable=True)


db.create_all()


@app.route('/')
@app.route('/login')
def login():
    return render_template('user/login.html')


@app.route('/join')
def join():
    return render_template('user/join.html')


@app.route('/user/join', methods=["POST"])
def setJoin():
    req = request.form
    email = req.get("email")
    password = req.get("password")
    first_name = req.get("first_name", None)
    last_name = req.get("last_name", None)
    gender = req.get("gender")


    userCount = User.query.filter_by(email=email).count()
    if userCount == 0:
        newUser = User(email=email, password=password, first_name=first_name, last_name=last_name, gender=gender)
        db.session.add(newUser)
        db.session.commit()

        return render_template('user/login.html', email=email)
    else:
        return render_template('user/join.html', errorMsg="존재하는 이메일 입니다.")



@app.route("/user/login", methods=["POST"])
def checkUser():
    # if request.method == 'POST':
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
