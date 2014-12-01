# coding: utf-8

"""
    wima.tests.test_events
    ======================

    Analytics events related tests.

    :copyright: Copyright (c) 2014 Andrey Martyanov. All rights reserved.
    :license: MIT, see LICENSE for more details.
"""

from wima.app import create_app
from wima.views import PIXEL


def test_pixel():
    app = create_app()

    with app.test_client() as c:
        r = c.get('/events/')
        assert r.status_code == 404

        r = c.get('/events/abcd')
        assert r.status_code == 200
        assert r.content_type == 'image/gif'
        assert r.data == PIXEL
