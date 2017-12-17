# -*- coding: utf-8 -*-


import hashlib
from urllib.parse import urlencode

import requests


class Request(object):

    def __init__(self, host=None, apikey=None, secret=None):
        """
        Constructor for class of HttpsRequest.
        :param url: Base URL for the Request methods
        :return: None
        """
        host = 'https://www.okex.com' if host is None else host.rstrip('/')
        self.__url = host
        self.apikey = apikey
        self.secret = secret

    def _sign(self, params):
        """
        To build MD5 sign for user's parameters.
        :param params: User's parameters usually in the format of a dict
        :param secret_key: String of SECRET KEY
        :return: Signed string encrypted by MD5
        """
        sign = {}

        if isinstance(params, dict):
            for key in sorted(params.keys()):
                sign[key] = str(params[key])

            data = sign
            data['secret_key'] = self.secret
            data = urlencode(sign, doseq=False, safe='', encoding=None, errors=None)
        else:
            raise TypeError('{0} should has attributes of "items"'.format(params))

        return hashlib.md5(data.encode('utf8')).hexdigest().upper()

    def get(self, endpoint, params=None):
        """
        GET method to request endpoints.
        :param endpoint: String of URL for endpoints
        :param params: String of user's parameters without encryption
        :return: JSON of the response of the GET request
        """

        path = '%s/%s' % (self.__url, endpoint.lstrip('/'))
        resp = requests.get(url=path, params=params)

        try:
            return resp.json()
        except ValueError as e:
            raise e
        except requests.HTTPError as e:
            if resp.status_code == '403':
                return '用户请求过快，可能IP被屏蔽'
            
            raise e

    def post(self, endpoint, params=None, sign=False):
        """
        POST method to request endpoints.
        :param endpoint: String of URL for endpoints
        :param data: User's parameters to be encrypted, usually in the format of a dict
        :return: Response of the GET request
        """
        params['api_key'] = self.apikey
        params['sign'] = self._sign(params)

        path = '%s/%s' % (self.__url, endpoint.lstrip('/'))
        resp = requests.post(url=path, data=params)

        try:
            return resp.json()
        except ValueError as e:
            raise e
        except requests.HTTPError as e:
            if resp.status_code == '403':
                return '用户请求过快，可能IP被屏蔽'
            
            raise e
