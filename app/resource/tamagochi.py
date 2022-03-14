import flask_praetorian
from flask import request

from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from .init_guard import guard
from app.models import User, Tamagochi
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
        user.tamagochi.game += 0.2
        if user.tamagochi.game > 1:
            user.tamagochi.game = 1
        user.tamagochi.general_state = 0.3 * user.tamagochi.sleep + 0.3 * user.tamagochi.food + \
                                          0.2 * user.tamagochi.game + 0.2 * user.tamagochi.health
        db.session.add(user)
        db.session.commit()
        return user.tamagochi


@tamagochi_ns.route("/food")
class TamagochiFoodResource(Resource):
    @flask_praetorian.auth_required
    @tamagochi_ns.doc('Get posts', security='Bearer')
    @responds(schema=TamagochiSchema, api=tamagochi_ns)
    def post(self):
        user_id = guard.extract_jwt_token(guard.read_token())['id']
        user = User.query.get(user_id)
        user.tamagochi.food += 0.2
        if user.tamagochi.food > 1:
            user.tamagochi.food = 1
        user.tamagochi.general_state = 0.3 * user.tamagochi.sleep + 0.3 * user.tamagochi.food + \
                                          0.2 * user.tamagochi.game + 0.2 * user.tamagochi.health
        db.session.add(user)
        db.session.commit()
        return user.tamagochi


@tamagochi_ns.route("/health")
class TamagochiHealthResource(Resource):
    @flask_praetorian.auth_required
    @tamagochi_ns.doc('Get posts', security='Bearer')
    @responds(schema=TamagochiSchema, api=tamagochi_ns)
    def post(self):
        user_id = guard.extract_jwt_token(guard.read_token())['id']
        user = User.query.get(user_id)
        user.tamagochi.health += 0.2
        if user.tamagochi.health > 1:
            user.tamagochi.health = 1
        user.tamagochi.general_state = 0.3 * user.tamagochi.sleep + 0.3 * user.tamagochi.food + \
                                          0.2 * user.tamagochi.game + 0.2 * user.tamagochi.health
        db.session.add(user)
        db.session.commit()
        return user.tamagochi


@tamagochi_ns.route("/sleep")
class TamagochiSleepResource(Resource):
    @flask_praetorian.auth_required
    @tamagochi_ns.doc('Get posts', security='Bearer')
    @responds(schema=TamagochiSchema, api=tamagochi_ns)
    def post(self):
        user_id = guard.extract_jwt_token(guard.read_token())['id']
        user = User.query.get(user_id)
        user.tamagochi.sleep += 0.2
        if user.tamagochi.sleep > 1:
            user.tamagochi.sleep = 1
        user.tamagochi.general_state = 0.3 * user.tamagochi.sleep + 0.3 * user.tamagochi.food + \
                                          0.2 * user.tamagochi.game + 0.2 * user.tamagochi.health
        db.session.add(user)
        db.session.commit()
        return user.tamagochi


@tamagochi_ns.route("/")
class TamagochiAdminEditorResource(Resource):
    @flask_praetorian.roles_required('admin')
    @tamagochi_ns.doc('Get posts', params={'user_id': 'Id хозяина тамагочи'},
                      security='Bearer')
    @accepts(schema=TamagochiSchema, api=tamagochi_ns)
    @responds(schema=TamagochiSchema, api=tamagochi_ns)
    def put(self):
        user_id = request.args.get('user_id')
        tamagochi = Tamagochi.query.filter(Tamagochi.user_id == user_id).first()
        new_tamagochi = request.parsed_obj
        tamagochi.sleep = new_tamagochi.sleep
        tamagochi.food = new_tamagochi.food
        tamagochi.game = new_tamagochi.game
        tamagochi.health = new_tamagochi.health
        tamagochi.general_state = 0.3 * tamagochi.sleep + 0.3 * tamagochi.food + \
                                          0.2 * tamagochi.game + 0.2 * tamagochi.health
        db.session.add(tamagochi)
        db.session.commit()
        return tamagochi
