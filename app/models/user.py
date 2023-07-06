from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    verified = db.Column(db.Boolean, default=False)
    remaining_count = db.Column(db.Integer, default=10)
    name = db.Column(db.String(64))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        print('password:', password)
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # @login_manager.user_loader
    # def load_user(self, user_id):
    #     return User.query.get(int(user_id))

    def get_by_email(self, email):
        return self.query.filter_by(email=email).first()

    def create_user(self):
        if not self.get_by_email(self.email):
            db.session.add(self)
            db.session.commit()
            return True
        return False

    def verify_email(self):
        self.verified = True
        db.session.commit()

    def update_remaining_count(self, count):
        self.remaining_count = count
        db.session.commit()

    def update_name(self, name):
        self.name = name
        db.session.commit()
