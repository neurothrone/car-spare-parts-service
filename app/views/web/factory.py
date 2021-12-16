import os
from typing import Type

import flask

from app.views.web.config import Config
from app.views.web.routes import bp


def create_app(config: Type[Config] = None,
               debug: bool = False,
               testing: bool = False,
               secure: bool = False,
               propagate_exceptions: bool = False) -> flask.Flask:
    _app = flask.Flask(__name__)
    _app.register_blueprint(bp)

    if config:
        _app.config.from_object(config)
        return _app

    _app.config["DEBUG"] = True if debug else False
    _app.config["TESTING"] = True if testing else False
    _app.config["SECRET_KEY"] = os.urandom(24) if secure else None
    _app.config["PROPAGATE_EXCEPTIONS"] = True if propagate_exceptions else False

    return _app
