import marshmallow_dataclass

from app.models.update_password_data import UpdatePasswordData

UpdatePasswordDataSchema = marshmallow_dataclass.class_schema(UpdatePasswordData)