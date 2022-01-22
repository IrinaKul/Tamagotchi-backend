from marshmallow import fields

from app.models import User
from .tamagochi import TamagochiSchema
from .init_ma import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        include_relationship = True

    tamagochi = fields.Nested(TamagochiSchema, dump_only=True, many=True)
    hashed_password = ma.auto_field(load_only=True)
    roles = ma.auto_field(load_only=True)
