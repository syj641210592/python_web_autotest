'''
Description: 登录页面功能操作
Author: sunwang
Date: 2020-09-29 22:40:38
LastEditTime: 2020-09-30 23:23:35
LastEditors: sunwang
'''
from html_page.base_page import BasePage
class LoginPage(BasePage):
    '''
    description: 登录页面封装
    '''

    def __init__(self, driver, url, sleep_time=10):
        super().__init__(driver, url, sleep_time)

    def login(self, user, pwd):
        '''登录'''
        # 定位登录框
        self.find_ele("XPATH", r'//input[@name = "phone"]')
        # 输入账号
        self.send_keys(user)
        # 定位密码框
        self.find_ele("XPATH", r'//input[@name = "password"]')
        # 输入账号
        self.send_keys(pwd)
        # 定位登录并点击
        self.find_ele("XPATH", r'//button[text()= "登录"]').click()


    

