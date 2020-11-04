'''
Description: 
Author: sunwang
Date: 2020-09-14 21:14:13
LastEditTime: 2020-11-04 23:34:00
LastEditors: sunwang
'''
from com_func.confread import config
import os

class TestPath(object):

    def __init__(self) :
        self.BasePath = os.getcwd()
        self.ScreenShot = os.path.join(os.sep, self.BasePath, config.get("ENV", "screenshot_path"))
        self.ReportPath = os.path.join(os.sep, self.BasePath, config.get("ENV", "report_path"))
        self.LogDirPath = os.path.join(os.sep, self.BasePath, config.get("ENV", "log_path"))
        self.TestData = os.path.join(os.sep, self.BasePath, "test_case_data", "case_data.yaml")


testpath = TestPath()