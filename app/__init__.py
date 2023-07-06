from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import os

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
chat_histories = {}


def create_app():
    app = Flask(__name__)
    base_dir = os.path.abspath(os.path.dirname(__file__))  # 获取项目的根目录的绝对路径
    database_path = os.path.join(base_dir, 'database')
    if not os.path.exists(database_path):
        os.makedirs(database_path)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'database/database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = 'your-secret-key-hh11'  # replace 'your-secret-key' with your own secret key

    db.init_app(app)
    login_manager.init_app(app)

    # migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    from app.models import User
    from app.routes import auth

    import app.view as view
    app.register_blueprint(view.main)
    import app.routes.auth as auth
    app.register_blueprint(auth.auth)

    import app.routes.mychatgpt as mychatgpt
    app.register_blueprint(mychatgpt.chat)

    return app
