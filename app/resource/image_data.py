import flask_praetorian

from flask import request
from flask_accepts import accepts, responds
from flask_restx import Resource, Namespace

from app.models.db_init import db
from app.models.image_data import ImageData
from app.schema.image_data import ImageDataSchema

imagedata_ns = Namespace('image_data', description='Данные для внешнего вида')

images_schema = ImageDataSchema(many=True)
image_schema = ImageDataSchema()


@imagedata_ns.route("/")
class ImagesResource(Resource):
    @imagedata_ns.doc('Список всех картинок')
    @responds(schema=images_schema, api=imagedata_ns)
    def get(self):
        return ImageData.query.all()

    @flask_praetorian.roles_required('admin')
    @imagedata_ns.doc('Добавление картинки', security='Bearer')
    @accepts(schema=image_schema, api=imagedata_ns)
    @responds(schema=image_schema, api=imagedata_ns)
    def post(self):
        data = request.parsed_obj
        db.session.add(data)
        db.session.commit()
        return data


@imagedata_ns.route("/<int:image_id>")
class ImageResource(Resource):
    @imagedata_ns.doc('Получение картинки по image_id')
    @responds(schema=image_schema, api=imagedata_ns)
    def get(self, image_id):
        return ImageData.query.get(image_id)

    @flask_praetorian.roles_required('admin')
    @imagedata_ns.doc('Изменение картинки', security='Bearer')
    @accepts(schema=image_schema, api=imagedata_ns)
    @responds(schema=image_schema, api=imagedata_ns)
    def put(self, image_id):
        data = request.parsed_obj
        img = ImageData.query.get(image_id)
        img.url = data.url
        img.text = data.text
        img.title = data.title
        db.session.add(img)
        db.session.commit()
        return img

    @flask_praetorian.roles_required('admin')
    @imagedata_ns.doc('Удаление картинки', security='Bearer')
    # @accepts(schema=image_schema, api=imagedata_ns)
    @responds(schema=image_schema, api=imagedata_ns)
    def delete(self, image_id):
        img = ImageData.query.get(image_id)
        db.session.delete(img)
        db.session.commit()
        return {'status': 'ok'}
