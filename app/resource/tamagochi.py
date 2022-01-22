import flask_praetorian

from flask_accepts import responds
from flask_restx import Namespace, Resource

from .init_guard import guard
from app.models import User
from app.models.db_init import db
from app.schema.tamagochi import TamagochiSchema

tamagochi_ns = Namespace('tamagochi', description='Операции для взаимодействия с тамагочи')


@tamagochi_ns.route("/game")
class TamagochiGameResource(Resource):
    @flask_praetorian.auth_required
    @tamagochi_ns.doc('Get posts', security='Bearer')
    @responds(schema=TamagochiSchema, api=tamagochi_ns)
    def post(self):
        user_id = guard.extract_jwt_token(guard.read_token())['id']
        user = User.query.get(user_id)
        user.tamagochi[0].game += 0.2
        if user.tamagochi[0].game > 1:
            user.tamagochi[0].game = 1
        user.tamagochi[0].general_state = 0.3 * user.tamagochi[0].sleep + 0.3 * user.tamagochi[0].food + \
                                          0.2 * user.tamagochi[0].game + 0.2 * user.tamagochi[0].health
        db.session.add(user)
        db.session.commit()
        return user.tamagochi[0]


@tamagochi_ns.route("/food")
class TamagochiFoodResource(Resource):
    @flask_praetorian.auth_required
    @tamagochi_ns.doc('Get posts', security='Bearer')
    @responds(schema=TamagochiSchema, api=tamagochi_ns)
    def post(self):
        user_id = guard.extract_jwt_token(guard.read_token())['id']
        user = User.query.get(user_id)
        user.tamagochi[0].food += 0.2
        if user.tamagochi[0].food > 1:
            user.tamagochi[0].food = 1
        user.tamagochi[0].general_state = 0.3 * user.tamagochi[0].sleep + 0.3 * user.tamagochi[0].food + \
                                          0.2 * user.tamagochi[0].game + 0.2 * user.tamagochi[0].health
        db.session.add(user)
        db.session.commit()
        return user.tamagochi[0]


@tamagochi_ns.route("/health")
class TamagochiHealthResource(Resource):
    @flask_praetorian.auth_required
    @tamagochi_ns.doc('Get posts', security='Bearer')
    @responds(schema=TamagochiSchema, api=tamagochi_ns)
    def post(self):
        user_id = guard.extract_jwt_token(guard.read_token())['id']
        user = User.query.get(user_id)
        user.tamagochi[0].health += 0.2
        if user.tamagochi[0].health > 1:
            user.tamagochi[0].health = 1
        user.tamagochi[0].general_state = 0.3 * user.tamagochi[0].sleep + 0.3 * user.tamagochi[0].food + \
                                          0.2 * user.tamagochi[0].game + 0.2 * user.tamagochi[0].health
        db.session.add(user)
        db.session.commit()
        return user.tamagochi[0]


@tamagochi_ns.route("/sleep")
class TamagochiSleepResource(Resource):
    @flask_praetorian.auth_required
    @tamagochi_ns.doc('Get posts', security='Bearer')
    @responds(schema=TamagochiSchema, api=tamagochi_ns)
    def post(self):
        user_id = guard.extract_jwt_token(guard.read_token())['id']
        user = User.query.get(user_id)
        user.tamagochi[0].sleep += 0.2
        if user.tamagochi[0].sleep > 1:
            user.tamagochi[0].sleep = 1
        user.tamagochi[0].general_state = 0.3 * user.tamagochi[0].sleep + 0.3 * user.tamagochi[0].food + \
                                          0.2 * user.tamagochi[0].game + 0.2 * user.tamagochi[0].health
        db.session.add(user)
        db.session.commit()
        return user.tamagochi[0]
