# -*- coding: utf-8 -*-

from .context import ENDPOINT
from .helpers import Request

# api = OKExAPI(apikey, secret)
# api.post('future_userinfo', params=None)
# api.get('userinfo', params=None)

class OKExAPI(object):
    """
    基础类
    """

    def __init__(self, apikey, secret):
        """
        Constructor for class of OKExBase.
        :param apikey: String of API KEY
        :param secret: String of SECRET KEY
        :return: None
        """
        self._request = Request(apikey=apikey, secret=secret)

    def post(self, endpoint=None,  *args, **kwargs):
        try:
            endpoint = '/api/v1/{}.do'.format(endpoint)
            res = self._request.post(endpoint, kwargs)
            return res
        except Exception as e:
            raise e

    def get(self, endpoint=None,  *args, **kwargs):
        try:
            endpoint = '/api/v1/{}.do'.format(endpoint)
            res = self._request.get(endpoint, kwargs)
            return res
        except Exception as e:
            raise e

    def call(self, endpoint=None, method='get', *args, **kwargs):
        
        try:
            endpoint = '/api/v1/{}.do'.format(endpoint)

            if method == 'post':
                res = self._request.post(endpoint, kwargs, True)
            else:
                res = self._request.get(endpoint, kwargs)

            return res
        except Exception as e:
            raise e
