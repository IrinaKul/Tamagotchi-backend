from marshmallow import fields

from app.models import Tamagochi
from .init_ma import ma


class TamagochiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tamagochi
        load_instance = True
        include_fk = True

    id = ma.auto_field(dump_only=True)
    user_id = ma.auto_field(dump_only=True)
    general_state = ma.auto_field(dump_only=True)


class TamagochiSchemaWithoutId(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tamagochi
        load_instance = True
        include_fk = True

    id = ma.auto_field(load_only=True)
    user_id = ma.auto_field(dump_only=True)
    general_state = ma.auto_field(dump_only=True)
