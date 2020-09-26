'''
Description: wen自动化
Author: sunwang
Date: 2020-09-14 21:04:05
LastEditTime: 2020-09-26 07:50:19
LastEditors: sunwang
'''
from testcase import testcase_login
from unittestreport import TestRunner

import unittest

# 测试套件
suit = unittest.TestSuite()
# 用例加载器
loder = unittest.TestLoader()
# 添加用例
suit.addTest(loder.loadTestsFromModule(testcase_login))

if __name__ == '__main__':
    # 测试报告
    run = TestRunner(suit, tester="孙忘", desc="孙忘产生的测试报告")
    run.run()