#!/usr/bin/env python
# coding: utf-8
from Public.email_send import send_mali_byQQ, send_mali_by163
from testCase.ddt_case import MyTest
import unittest, time, os
from Public import BSTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    now = time.strftime('%Y-%m%d-%H%M', time.localtime(time.time()))
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'test_Report')
    file = os.path.join(file_dir, (now + '.html'))
    re_open = open(file, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='http接口测试报告', description='测试结果')
    m = runner.run(suite)
    contec = 'http接口自动化测试完成，测试通过:%s,测试失败：%s，未知错误：%s,详情见：%s' % (m.success_count, m.failure_count, m.error_count, file)
    send_mali_byQQ("776133011@qq.com", "ywhfmrqenhqcbdbb","274859299@qq.com","123", file)
    send_mali_by163("Avey777@163.com", "Amie940516","18776315209@163.com","123", file)
