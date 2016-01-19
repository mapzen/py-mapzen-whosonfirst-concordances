# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
# __import__('pkg_resources').declare_namespace(__name__)

import sys
import logging

import json
import requests

class db:

    def __init__ (self, **kwargs):

        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('host', 8228)

    def execute_request(self, params):

        url = "http://%s:%s" % (self.host, self.port)
        rsp = requests.get(url, params=params)

        return json.decode(rsp.content)
        
class query(db):

    def foo(self):
        pass

