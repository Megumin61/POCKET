from flask import Blueprint,request
from database import *
session_bp=Blueprint('session',__name__,url_prefix='/session')

@session_bp.route('',methods=['POST'])
def login():
    data=request.get_json(force=True)
    username=data.get('username')
    password=data.get('password')
    check_inf(username,password)
    return '登录成功'