'''
Description: 登录页面功能操作
Author: sunwang
Date: 2020-09-29 22:40:38
LastEditTime: 2020-10-01 16:05:04
LastEditors: sunwang
'''
from html_page.page_locator import locator_login
from html_page.base_page import BasePage
from com_func.confread import config


class LoginPage(BasePage):
    '''
    description: 登录页面封装
    '''

    def fresh(self):
        '''刷新网页'''
        super().fresh(config.get("URL", "base_url")+config.get("URL", "login_url"))

    def login(self, user, pwd):
        '''登录'''
        # 定位登录框
        self.find_ele(*locator_login.user)
        # 输入账号
        self.send_keys(user)
        # 定位密码框
        self.find_ele(*locator_login.pwd)
        # 输入账号
        self.send_keys(pwd)
        # 定位登录并点击
        self.find_ele(*locator_login.login).click()


    

