from .db_init import db


class ImageData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000))
    title = db.Column(db.String(1000))
    text = db.Column(db.String(1000))
