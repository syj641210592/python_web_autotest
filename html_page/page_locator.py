'''
Description: 定位元素locator
Author: sunwang
Date: 2020-10-02 06:50:13
LastEditTime: 2020-10-02 06:59:52
LastEditors: sunwang
'''


from selenium.webdriver.common.by import By

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
    description:登录页面locator 
    param : 
    return {type} 
    '''
    def __init__(self):
        self.invest = ("XPATH", r'//span[text()=" 测试1602388207796"]/ancestor::div[2]//a[text()="抢投标"]')
        self.money_input = ("XPATH", r'//input[@class="form-control invest-unit-investinput"]')
        self.tender = ("XPATH", r'//button[text()="投标"]')
        self.islogin = ("XPATH", f"//a[text()={user}]")
        self.quit = ("XPATH", r"//a[text()='退出']")
locator_login = LocatorLogin()
locator_home = LocatorHome()