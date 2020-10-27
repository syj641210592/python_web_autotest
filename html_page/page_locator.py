'''
Description: 定位元素locator
Author: sunwang
Date: 2020-10-02 06:50:13
LastEditTime: 2020-10-02 06:59:52
LastEditors: sunwang
'''


from selenium.webdriver.common.by import By
from com_func.confread import config

class LocatorLogin(object):
    '''
    description:登录页面locator 
    param : 
    return {type} 
    '''
    def __init__(self):
        self.user = ("XPATH", r'//input[@name = "phone"]')
        self.pwd = ("XPATH", r'//input[@name = "password"]')
        self.login = ("XPATH", r'//button[text()= "登录"]')

class LocatorHome(object):
    '''
    description:首页locator 
    param : 
    return {type} 
    '''
    def __init__(self):
        self.invest = ("XPATH", r'//span[text()=%s]/ancestor::div[2]//a[text()="抢投标"]' % config.get("PRESENT", "inverst_name"))  # 抢投标
        self.islogin = ("XPATH", f"//a[text()={user}]")  # 登录用户显示
        self.quit = ("XPATH", r'//a[text()="退出"]')  # 退出登录

class LocatorInverst(object):
    '''
    description:投资locator 
    param : 
    return {type} 
    '''
    def __init__(self):
        self.money_input = ("XPATH", r'//input[@class="form-control invest-unit-investinput"]')  # 金额输入
        self.tender_button = ("XPATH", r'//button[text()="投标"]')  # 投标按钮
        self.set_all = ("XPATH", r'//input[@class="set-all"]')  # 全投按钮
locator_login = LocatorLogin()
locator_home = LocatorHome()
locator_inverst = LocatorInverst()