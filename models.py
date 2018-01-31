from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    habits = db.relationship('Habit', backref='user', lazy='dynamic')
    settings = db.relationship('Settings', backref='user', uselist=False)


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_of_week = db.Column(db.Integer, default=1)
    start_of_month = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # _user = db.relationship('User', back_populates="settings")


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    habit = db.Column(db.String(120), nullable=False)
    dates = db.relationship('DateEvent', backref='habit', lazy='dynamic')


class DateEvent(db.Model):
    date = db.Column(db.Date, primary_key=True)
    is_complete = db.Column(db.Boolean, nullable=False, default=0)
    is_active = db.Column(db.Boolean, nullable=False, default=1)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'))
