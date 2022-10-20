#!/usr/bin/env python3

import json
from kivy.network.urlrequest import UrlRequest

key = "12f0a89ef48f0f7b35f2c819139f15ec"


class NetworkException(Exception):
    pass


class ApiException(Exception):
    pass


class ApiClient():
    def __init__(self, post_url='2captcha.com'):
        self.post_url = post_url

    def in_(self, files={}, **kwargs):
        current_url = 'https://'+self.post_url+'/in.php'
        data = json.dumps(kwargs)
        resp = UrlRequest(current_url, req_body=data)
        resp.wait()
        return resp._result

    def res(self, **kwargs):
        key = kwargs['key']
        action = kwargs['action']
        id = kwargs['id']
        current_url_out = 'https://'+self.post_url + \
            '/res.php?key='+key+'&action='+action+'&id='+id
        resp = UrlRequest(current_url_out)
        resp.wait()
        return resp._result
