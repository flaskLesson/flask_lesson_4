from flask import Blueprint, render_template, request
from config import initClass

user_bp = Blueprint("user", __name__)

@user_bp.route('/')
@user_bp.route('/login')
def index():
    return render_template('user/login.html')


@user_bp.route("/user/login", methods=["POST"])
def login():
    if request.method == 'POST':
        req = request.form

        # 데이터 받기
        email = req.get("email")
        pw = req.get("password")

        # 서버 연결
        row = User.query.filter_by(id=84723726).first()
        print(row)

        return render_template('user/login.html')
