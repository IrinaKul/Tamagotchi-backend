from app.models import ImageData
from app.schema.init_ma import ma


class ImageDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ImageData
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)
