# coding: utf-8

"""
    wima.views
    ==========

    Project views.

    :copyright: Copyright (c) 2014 Andrey Martyanov. All rights reserved.
    :license: MIT, see LICENSE for more details.
"""

import base64

from flask import Response, render_template

from flask.ext.classy import FlaskView, route


# Transparent 1x1 pixel GIF
PIXEL = base64.b64decode('R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAIAOw==')


class DashboardView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('dashboard.html')


class EventsView(FlaskView):

    @route('<string:app_id>')
    def get(self, app_id):
        return Response(PIXEL, mimetype='image/gif')
