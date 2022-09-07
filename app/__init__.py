from flask import Flask, request, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_mobility import Mobility
from flask_restx import Api
from flask_apscheduler import APScheduler

from . import resource
from .config import Config
from .models.db_init import db, get_session
from .resource.init_guard import guard
from .schema.init_ma import ma

cors = CORS()
migrate = Migrate()
scheduler = APScheduler()
mobility = Mobility()

api = Api(authorizations={
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    },
})

from .models import *


def create_app():
    config = Config  # Todo: fixme!!!

    app = Flask(__name__)
    app.config.from_object(config)
    app.debug = True
    from app.models import User
    with app.app_context():
        guard.init_app(app, User)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    api.init_app(app)
    mobility.init_app(app)
    api.add_namespace(resource.user_ns)
    api.add_namespace(resource.tamagochi_ns)
    api.add_namespace(resource.imagedata_ns)
    api.add_namespace(resource.applinks_ns)

    @app.after_request
    def after_request(response):
        if request.MOBILE:
            return redirect('https://drive.google.com/file/d/1wzsl152Nr9HBctG65mMoBuMDk3yCyMT6/view')
        return response

    cors.init_app(app)

    # initialize scheduler
    # if you don't wanna use a config, you can set options here:
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    return app


@scheduler.task('interval', id='do_job_1', minutes=5)
def downgrade_tamagochi_params():
    with get_session() as session:
        tamagochies = session.query(Tamagochi).all()
        for tamagochi in tamagochies:
            tamagochi.food = max(tamagochi.food - 0.1, 0)
            tamagochi.game = max(tamagochi.game - 0.1, 0)
            tamagochi.health = max(tamagochi.health - 0.1, 0)
            tamagochi.sleep = max(tamagochi.sleep - 0.1, 0)
            tamagochi.general_state = max(0.3 * tamagochi.sleep + 0.3 * tamagochi.food + \
                                          0.2 * tamagochi.game + 0.2 * tamagochi.health, 0)
            session.add(tamagochi)
            session.commit()
