#!/usr/bin/env python
# coding: utf-8

"""
    wima.wsgi
    =========

    Application WSGI handler.

    :copyright: Copyright (c) 2014 Andrey Martyanov. All rights reserved.
    :license: MIT, see LICENSE for more details.
"""

from wima.app import create_app


application = create_app()


if __name__ == '__main__':
    application.run()
