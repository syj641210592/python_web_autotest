'''
Author: sunwang
Date: 2020-09-26 06:20:47
LastEditTime: 2020-09-30 06:45:25
LastEditors: sunwang
Description: web自动化
FilePath: \python_web_autotest\testcase\testcase_login.py
'''

from logging import exception
import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from html_page.login_page import LoginPage
from com_func.confread import config
from selenium.webdriver import Edge 
import unittest
import ddt

test_data = [
    {"title": "账户密码错误_账户错误", "phone": "13018977985", "pwd": "python","xpath":"//div[text()='%s']", "expected": "帐号或密码错误!"},
    {"title": "账户密码错误_账户为空", "phone": "", "pwd": "python","xpath":"//div[text()='%s']", "expected": "请输入手机号"},
    {"title": "账户密码错误_密码为空", "phone": "13018977985", "pwd": "","xpath":"//div[text()='%s']", "expected": "请输入密码"},
    {"title": "账户密码正确", "phone": "18684720553", "pwd": "python","xpath":"//a[text()='%s']", "expected": "我的帐户[python]"}
]



@ddt.ddt
class Test_login(unittest.TestCase):
    '''
    description: 网页登录用例类
    param : 
    return {type} 
    '''
    @classmethod
    def setUpClass(cls):
        driver = Edge(exception=config.get("ENV", "drive_path"))
        url = r'http://120.78.128.25:8765/Index/login.html'
        cls.login = LoginPage(driver, url)
    
    def setUp(self):
        self.login.fresh()
    

    @ddt.data(*test_data)
    @ddt.unpack
    def test_login(self, title, **kwargs):
        '''{title}'''
        self.login.login(kwargs['phone'], kwargs['pwd'])
        res_ele = self.login.
        # 校验结果
        try:
            ele = self.driver.find_element(By.XPATH,  kwargs['xpath'] % kwargs['expected'])
        except Exception as e:
            ele = ""
        finally:
            self.assertTrue(ele)
    
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    


