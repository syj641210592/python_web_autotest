'''
Author: sunwang
Date: 2020-09-26 06:20:47
LastEditTime: 2020-09-26 07:48:05
LastEditors: sunwang
Description: web自动化
FilePath: \python_web_autotest\testcase\testcase_login.py
'''

import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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

test_data_sucess = [
    
]

@ddt.ddt
class Test_login(unittest.TestCase):
    '''
    description: 
    param : 
    return {type} 
    '''
    @classmethod
    def setUpClass(cls):
        # 设置访问地址
        cls.url = r'http://120.78.128.25:8765/Index/login.html'
        # 初始化浏览器
        cls.driver = Edge(executable_path=config.get('ENV', 'drive_path'))
        # 最大化窗口
        cls.driver.maximize_window()
        # 设置隐性等待
        cls.driver.implicitly_wait(10)
    
    def setUp(self):
        self.driver.get(self.url)
    

    @ddt.data(*test_data)
    @ddt.unpack
    def test_login(self, title, **kwargs):
        '''{title}'''
        # 输入账号
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, r'//input[@name = "phone"]'))
        ).send_keys(kwargs['phone'])
        # 输入密码
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, r'//input[@name = "password"]'))
        ).send_keys(kwargs['pwd'])
        # 点击登录
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, r'//button[text()= "登录"]'))
        ).click()
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
    


