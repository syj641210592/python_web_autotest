'''
Description: wen自动化
Author: sunwang
Date: 2020-09-14 21:04:05
LastEditTime: 2020-11-10 21:06:53
LastEditors: sunwang
'''


import pytest
pytest.main(['-s', '-v', "--html", "report.html", "--reruns", "3", "--reruns-delay", "5"])