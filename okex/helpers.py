# -*- coding: utf-8 -*-

# 用于进行https请求，以及 MD5 签名的工具类

import hashlib
import requests
from urllib.parse import urlencode

class Request(object):

    def __init__(self, url=None, key=None):
        """
        Constructor for class of HttpsRequest.
        :param url: Base URL for the Request methods
        :return: None
        """
        self.__url = url.rstrip('/')
        self.__key = key

    def __sign(self, params):
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
            data['secret_key'] = self.__key
            data = urlencode(sign, doseq=False, safe='', encoding=None, errors=None) 
        else:
            raise TypeError('{0} should has attributes of "items"'.format(params))
        
        return hashlib.md5(data.encode('utf8')).hexdigest().upper()

    def get(self, resource, params=None, sign=False):
        """
        GET method to request resources.
        :param resource: String of URL for resources
        :param params: String of user's parameters without encryption
        :return: JSON of the response of the GET request
        """
        if sign is True:
            params['sign'] = self.__sign(params)
        
        path = '%s/%s' % (self.__url, resource.lstrip('/'))
        resp = requests.get(url=path, params=params)
        data = resp.json()

        return data

    def post(self, resource, params=None, sign=False):
        """
        POST method to request resources.
        :param resource: String of URL for resources
        :param data: User's parameters to be encrypted, usually in the format of a dict
        :return: Response of the GET request
        """
        if sign is True:
            params['sign'] = self.__sign(params)
        
        path = '%s/%s' % (self.__url, resource.lstrip('/'))
        resp = requests.post(url=path, data=params)
        data = resp.content

        return data
