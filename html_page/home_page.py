'''
Description: 首页page页面操作
Author: sunwang
Date: 2020-10-01 12:05:40
LastEditTime: 2020-10-12 22:48:17
LastEditors: sunwang
'''
from html_page.page_locator import locator_home
from html_page.base_page import BasePage
from com_func.confread import config
class HomePage(BasePage):
    '''
    description: 登录页面封装
    '''

    def fresh(self, url=""):
        '''刷新网页'''
        BasePage.fresh(config.get("URL", "home_url"))

    def is_login(self, user):
        '''判断用户已经登录'''
        self.find_ele(*locator_home.islogin)

    def inverst(self, user):
        '''抢投标'''
        self.find_ele(*locator_home.invest).click()        

    def quit_login(self, user):
        '''退出登录'''
        self.find_ele(*locator_home.quit).click()
        