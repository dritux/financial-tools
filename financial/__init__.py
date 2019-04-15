# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from financial.config import config


def create_app(settings_override={}):
    app = Flask(__name__)

    app_env = os.getenv('FLASK_ENV', 'default')

    app.config.from_object(config[app_env])

    db.init_app(app)

    from financial.views.user import user
    app.register_blueprint(user)

    from financial.views.wallet import wallet
    app.register_blueprint(wallet)

    return app


ma = Marshmallow(create_app)
db = SQLAlchemy()
