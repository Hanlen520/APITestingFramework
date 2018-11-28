# -*- coding: utf-8 -*-
# @File    : 接口封装文件

from Public.test_requests import request
reques=request()

class TestApi(object):
	def __init__(self,url,key,connent,fangshi):
		self.url=url
		self.key=key
		self.connent=connent
		self.fangshi=fangshi
	def testapi(self):
		if self.fangshi=='POST':
			self.parem = {'key': self.key, 'info': self.connent}
			self.response=reques.post(self.url,self.parem)
		elif self.fangshi=="GET":
			self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.get(url=self.url,params=self.parem)
		return self.response
	def getJson(self):
		json_data = self.testapi()
		return json_data

if "__name__" == "__main__":

	api = TestApi(url="http://www.shangzhan168.cn" + "/Account/Login", connent={"hnAccount":"15020579521","hnPassword":"123456"}, fangshi="POST")
	apijson = api.getJson()
	print(api)
	print(apijson)