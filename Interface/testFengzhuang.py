#!/usr/bin/env python
# coding: utf-8
from Public.test_requests import requ

reques = requ()


class TestApi(object):
    def __init__(self, url, key, connent, fangshi):
        self.url = url
        self.key = key
        self.connent = connent
        self.fangshi = fangshi

    def testapi(self):
        if self.fangshi == 'POST':
            self.parem = {'key': self.key, 'info': self.connent}
            self.response = reques.post(self.url, self.parem)
        elif self.fangshi == "GET":
            self.parem = {'key': self.key, 'info': self.connent}
            self.response = reques.get(url=self.url, params=self.parem)
        return self.response

    def getJson(self):
        json_data = self.testapi()
        return json_data