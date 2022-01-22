from marshmallow import fields

from app.models import Tamagochi
from .init_ma import ma


class TamagochiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tamagochi
        load_instance = True
        include_fk = True
