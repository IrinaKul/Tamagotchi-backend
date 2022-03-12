from marshmallow import fields

from app.models import User
from .tamagochi import TamagochiSchemaWithoutId
from .init_ma import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        include_relationship = True

    tamagochi = fields.Nested(TamagochiSchemaWithoutId, dump_only=True)
    hashed_password = ma.auto_field(load_only=True)
    roles = ma.auto_field(load_only=True)
