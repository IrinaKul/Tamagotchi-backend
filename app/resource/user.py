import flask_praetorian
from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource, Namespace

from app.models import User, Tamagochi
from app.models.db_init import db
from app.resource.init_guard import guard
from app.schema import UserSchema, LoginDataSchema
from app.schema.registration_data import RegistrationDataSchema

user_ns = Namespace('user', description='Операции для взаимодействия с пользователями')


@user_ns.route("/login")
class UserLoginResource(Resource):
    @user_ns.doc('Login')
    @accepts(schema=LoginDataSchema, api=user_ns)
    def post(self):
        data = request.parsed_obj
        user = guard.authenticate(data.name, data.password)
        return {"access_token": guard.encode_jwt_token(user), 'id': user.id}


@user_ns.route("/registration")
class UserRegistrationResource(Resource):
    @user_ns.doc('Registration')
    @accepts(schema=RegistrationDataSchema, api=user_ns)
    @responds(schema=None, api=user_ns, status_code=200)
    def post(self):
        data = request.parsed_obj
        user = User(
            name=data.name,
            hashed_password=guard.hash_password(data.password),
            roles='user'
        )
        db.session.add(user)
        db.session.commit()
        tamagochi = Tamagochi(
            general_state=1,
            game=1,
            id=1,
            health=1,
            sleep=1,
            food=1,
            user_id=user.id
        )
        db.session.add(tamagochi)
        db.session.commit()
        return {'status': 'ok'}


@user_ns.route("/<int:user_id>")
class UserResource(Resource):
    @user_ns.doc('User data', security='Bearer')
    @responds(schema=UserSchema, api=user_ns, status_code=200)
    def get(self, user_id):
        return db.session.query(User).get(user_id)

    @flask_praetorian.roles_required('admin')
    @user_ns.doc('User data', security='Bearer')
    @responds(schema=UserSchema, api=user_ns, status_code=200)
    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'status': 'ok'}


@user_ns.route("/")
class AllUserRegistrationResource(Resource):
    @responds(schema=UserSchema, many=True, api=user_ns, status_code=200)
    def get(self):
        return User.query.all()
