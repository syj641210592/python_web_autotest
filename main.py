'''
Description: web自动化
Author: sunwang
Date: 2020-09-14 21:04:05
LastEditTime: 2020-12-15 22:53:33
LastEditors: sunwang
'''


import pytest
import os
pytest.main(['-s', '-v', "--reruns", "3", "--reruns-delay", "5" , "--alluredir=result/report"])
os.system('--alluredir=result/report')