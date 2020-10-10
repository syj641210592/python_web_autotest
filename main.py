'''
Description: wen自动化
Author: sunwang
Date: 2020-09-14 21:04:05
LastEditTime: 2020-10-10 22:53:32
LastEditors: sunwang
'''
# from testcase import test_case_login
# from com_func.basepath import testpath
# from unittestreport import TestRunner

# import unittest

# # 测试套件
# suit = unittest.TestSuite()
# # 用例加载器
# loder = unittest.TestLoader()
# # 添加用例
# suit.addTest(loder.loadTestsFromModule(test_case_login))

# if __name__ == '__main__':
#     # 测试报告
#     run = TestRunner(suit, tester="孙忘", desc="孙忘产生的测试报告", filename="report.html", report_dir=testpath.ReportPath)
#     run.run()

import pytest
pytest.main(['-s', '-v'])