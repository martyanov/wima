# coding: utf-8

"""
    wima.app
    ========

    Application factory and settings.

    :copyright: Copyright (c) 2014 Andrey Martyanov. All rights reserved.
    :license: MIT, see LICENSE for more details.
"""

import os

from flask import Flask

from .extensions import db
from .views import DashboardView


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'replace-me-with-real-secret-key'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    if os.environ.get('WIMA_CONF'):
        app.config.from_envvar('WIMA_CONF')
    else:
        path = os.path.normpath(os.path.expanduser('~/.wima.conf'))
        app.config.from_pyfile(path, silent=True)

    db.init_app(app)

    DashboardView.register(app)

    return app
