from .db_init import db


class UIData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    splashscreen_image_url = db.Column(db.String(1000))
