from flask import Blueprint, request, render_template, flash, redirect, url_for,current_app
from flask_login import login_user, logout_user, login_required
from app.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user is not None and user.verify_password(request.form['password']):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('confirm_password')
        print(username, email, password, password_confirm)
        # 在这里，你需要验证用户输入，比如检查两次密码输入是否一致
        if password != password_confirm:
            return "Passwords do not match.", 400
        # 然后，尝试创建新用户并保存到数据库中
        new_user = User(name=username, email=email)
        new_user.password = password  # 使用 User 模型中的 password 属性
        if new_user.create_user():  # 使用 User 模型中的 create_user() 方法
            # 如果用户创建成功，重定向用户到登录页面
            return redirect(url_for('auth.login'))
        else:
            # 如果用户创建失败（可能是因为邮箱已被注册），可以返回一个错误信息
            return "Email already registered.", 400
    return render_template('signup.html')  # 如果是GET请求，直接显示注册页面
