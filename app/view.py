#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('app.html')

#
# @main.route('/login')
# def login():
#     return render_template('login.html')

#
# @main.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         password_confirm = request.form.get('confirm_password')
#         print(username, email, password, password_confirm)
#         # 在这里，你需要验证用户输入，比如检查两次密码输入是否一致
#         if password != password_confirm:
#             return "Passwords do not match.", 400
#         # 然后，尝试创建新用户并保存到数据库中
#         new_user = User(name=username, email=email)
#         new_user.password = password  # 使用 User 模型中的 password 属性
#         if new_user.create_user():  # 使用 User 模型中的 create_user() 方法
#             # 如果用户创建成功，重定向用户到登录页面
#             return redirect(url_for('login'))
#         else:
#             # 如果用户创建失败（可能是因为邮箱已被注册），可以返回一个错误信息
#             return "Email already registered.", 400
#     return render_template('signup.html')  # 如果是GET请求，直接显示注册页面
