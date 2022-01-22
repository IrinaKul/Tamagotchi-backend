import flask_praetorian
from flask import request
from flask_accepts import accepts
from flask_restx import Resource, Namespace
from marshmallow import Schema, fields

from app.models.db_init import db
from app.models.ui_data import UIData

uidata_ns = Namespace('uidata', description='Данные для внешнего вида')


class UIDataSplashscreenImageURLSchema(Schema):
    splashscreen_image_url = fields.String()



@uidata_ns.route("/splashscreen_image_url")
class UIDataSplashscreenImageURLResource(Resource):
    @uidata_ns.doc('Сплешскрин')
    def get(self):
        if len(UIData.query.all()) == 0:
            uidata = UIData(splashscreen_image_url='')
            db.session.add(uidata)
            db.session.commit()

        uidata = UIData.query.first()
        return {"splashscreen_image_url": uidata.splashscreen_image_url}

    @flask_praetorian.roles_required('admin')
    @uidata_ns.doc('Сплешскрин', security='Bearer')
    @accepts(schema=UIDataSplashscreenImageURLSchema, api=uidata_ns)
    def post(self):
        if len(UIData.query.all()) == 0:
            uidata = UIData(splashscreen_image_url='')
            db.session.add(uidata)
            db.session.commit()

        uidata = UIData.query.first()
        uidata.splashscreen_image_url = request.json['splashscreen_image_url']
        db.session.add(uidata)
        db.session.commit()
        return {"splashscreen_image_url": uidata.splashscreen_image_url}
