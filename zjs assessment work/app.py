from flask import Flask, jsonify, request, session
from mysql.connector import connect
from werkzeug.security import generate_password_hash,check_password_hash
from database import *
from controller.users import users_bp
from controller.session import session_bp
import config
from utils import *
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

@app.route('/')
def hello_world():
    return 'Hello,World!!'

@app.errorhandler(HttpError)
def handle_http_error(error):
    response=jsonify(error.to_dict())
    response.status_code=error.status_code
    return response
#注册,改名字,改密码
app.register_blueprint(users_bp)
#登录
app.register_blueprint(session_bp)
if __name__ =='__main__':
    app.run()
