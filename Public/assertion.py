# -*- coding: utf-8 -*-
"""
encapsulation_dict:封装技术
anticipate 预期—数据
return 返回—数据
"""

"""断言方法封装"""
from Public.encapsulation_dict import res
from .log import LOG,logger

@logger('断言测试结果')
def assert_in(anticipate,return_json):
    if len(anticipate.split('=')) > 1:
        data = anticipate.split('&')
        result = dict([(item.split('=')) for item in data])
        value1=([(str(res(return_json,key))) for key in result.keys()])
        value2=([(str(value)) for value in result.values()])
        print(value1)
        print(value2)
        if value1==value2:
            return  { 'code':0,"result":'pass'}
        else:
            return {'code':1,'result':'fail'}
    else:
        LOG.info('断言错误，请填写测试预期值')
        return  {"code":2,'result':'断言错误，请填写测试预期值'}


@logger('断言测试结果')
def assertre(anticipate):
    if len(anticipate.split('=')) > 1:
        data = anticipate.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info('断言，填写测试预期值')
        raise {"code":1,'result':'断言，填写测试预期值'}