#database.py
#操作数据库
from flask import Flask,jsonify,request,session
from mysql.connector import connect
from werkzeug.security import generate_password_hash,check_password_hash
from utils import *

def get_connection():
    conn=connect(user='root',password='',database='bbt')
    cursor=conn.cursor()
    return conn,cursor
def check_username_is_exit(username):
    conn,cursor=get_connection()
    cursor.execute('select count(*) from `users` where `username`=%s',(username,) )
    count=cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count
def save_user(username,password):
    count=check_username_is_exit(username)
    if count >=1:
        raise HttpError(409,'用户名已注册!')
    conn,cursor=get_connection()
    cursor.execute('insert into `users`(`username`,`password`) values (%s,%s)',
                   (username,generate_password_hash(password)))
    conn.commit()
    conn.close()
    cursor.close()
def check_inf(username,password):
    conn, cursor = get_connection()
    cursor.execute('select `id`,`password` from `users` where `username`=%s', (username,))
    values = cursor.fetchone()
    if values is None:
        raise HttpError(400, '用户名或密码错误')
    user_id = values[0]
    pwd = values[1]
    if not check_password_hash(pwd, password):
        raise HttpError(400, '用户名或密码错误')
    session['username']=username
    session['user_id']=user_id
    session['password'] =password
    return "登录成功"


def change_name(username):
    conn, cursor = get_connection()
    if session.get('user_id') is None:
        raise HttpError(401, '请先登录')

    cursor.execute('select count(*) from `users` where `username`=%s', (username,))
    count = cursor.fetchone()[0]
    if count >= 1:
        raise HttpError(409, '用户名已存在')
    cursor.execute('update `users` set `username`=%s where id=%s', (username, session.get('user_id')))
    conn.commit()
    cursor.close()
    conn.close()
def change_word(password):
    conn, cursor = get_connection()
    if session.get('user_id') is None:
        raise HttpError(401, '请先登录')
    if password==session.get('password'):
        return '密码重复!'
    else:
        cursor.execute('update `users` set `password`=%s where id=%s',
                   (generate_password_hash(password), session.get('user_id')))
        conn.commit()
        cursor.close()
        conn.close()
        return '修改密码成功'
def p_passage(content,permission):
    conn, cursor = get_connection()
    cursor.execute('update `users` set `passages`=%s where id=%s', (content, session.get('user_id')))
    cursor.execute('update `users` set `permission`=%s where id=%s', (permission, session.get('user_id')))
    conn.commit()
    cursor.close()
    conn.close()
def c_passage(content):
    conn, cursor = get_connection()
    cursor.execute('update `users` set `passages`=%s where id=%s', (content, session.get('user_id')))
    conn.commit()
    cursor.close()
    conn.close()
def d_passage(content):
    conn, cursor = get_connection()
    cursor.execute('delete passage from `users` where `id`=%s', (session.get('user_id',)))
    conn.commit()
    cursor.close()
    conn.close()
def de_users(username):
    conn, cursor = get_connection()
    if session.get('username',) == 'admin':
        cursor.execute('delete from users where `username`=%s',username)
        conn.commit()
        cursor.close()
        conn.close()
        return '用户 %s 已经被删除！！' % username

    if username != 'admin':
        conn.commit()
        cursor.close()
        conn.close()
        return '没有该用户...'
def s_passages(id):
    conn, cursor = get_connection()
    cursor.execute('select `passages` from `users` where `id`=%s', (id,))
    content = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return content













