# coding: utf-8

"""
    wima.views
    ==========

    Project views.

    :copyright: Copyright (c) 2014 Andrey Martyanov. All rights reserved.
    :license: MIT, see LICENSE for more details.
"""

from flask import render_template

from flask.ext.classy import FlaskView


class IndexView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('index.html')
