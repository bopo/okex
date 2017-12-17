# -*- coding: utf-8 -*-

try:
    import sys
    import os

    from okex.context import *
    from okex.core import OKExMarketAPI, OKExTraderAPI
except ImportError:
    pass

APIKEY = os.environ.get('APIKEY', None)
SECRET = os.environ.get('SECRET', None)
