from flask import Blueprint,request
from database import *

users_bp=Blueprint('users',__name__,url_prefix='/users')


@users_bp.route('',methods=['POST'])
def register():
    data=request.get_json(force=True)
    username=data.get('username')
    password=data.get('password')
    save_user(username,password)
    return '创建成功!'

@users_bp.route('/username',methods=['PUT'])
def change_username():
    data=request.get_json(force=True)
    username=data.get('username')
    change_name(username)
    return '修改用户名成功'

@users_bp.route('/password',methods=['PUT'])
def change_password():
    data=request.get_json(force=True)
    password=data.get('password')
    return change_word(password)
@users_bp.route('/check_users',methods=['GET'])
def check_users_infor():
    if session.get('user_id') is None:
        raise HttpError(401,'请先登录')
    return {
            'user_id':session.get('user_id'),
            'username':session.get('username')
        }
@users_bp.route('/post_passage',methods=['POST'])
def post_passage(permission=0):
    data=request.get_json(force=True)
    content=data.get('content')
    permission=data.get('permission')
    p_passage(content,permission)
    return '发布成功！'
@users_bp.route('/change_passage',methods=['PUT'])
def change_passage():
    data = request.get_json(force=True)
    content = data.get('content')
    c_passage(content)
    return '修改成功!'
@users_bp.route('/delete_passage',methods=['PUT'])
def delete_passage():
    data = request.get_json(force=True)
    content = data.get('content')
    d_passage(content)
    return '删除成功!'
@users_bp.route('/get_passage',methods=['GET'])
def get_passage():
    conn, cursor = get_connection()
    cursor.execute('select `passages` from `users` where `id`=%s', (session.get('user_id'),))
    content=cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return content
@users_bp.route('/admin',methods=['POST'])
def delete_users():
    data=request.get_json(froce=True)
    username=data.get('username')
    return de_users(username)
@users_bp.route('/see',methods=['GET'])
def see_passages():
    if permission==0:
        data=request.get_json(froce=True)
        passage_id=data.get('passage_id')
        return s_passages()
    if permission==1:
        return '没有权限'










