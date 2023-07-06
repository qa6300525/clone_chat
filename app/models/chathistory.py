#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
from app import db


class ChatHistory(db.Model):
    __tablename__ = 'chat_histories'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True)
    bot_type_str = db.Column(db.String(36))  # 模型类型，确定之后不能改变
    session_id = db.Column(db.String(36))  # Assuming UUID is used for session_id
    message = db.Column(db.Text)
    sender = db.Column(db.String(10))  # Assuming 'system', 'user' or 'bot' as possible values
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def save_message(self):
        db.session.add(self)
        db.session.commit()
