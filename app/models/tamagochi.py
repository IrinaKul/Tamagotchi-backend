from .db_init import db


class Tamagochi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sleep = db.Column(db.Float)
    food = db.Column(db.Float)
    game = db.Column(db.Float)
    health = db.Column(db.Float)
    general_state = db.Column(db.Float)
    name = db.Column(db.String)
    gender = db.Column(db.String)
