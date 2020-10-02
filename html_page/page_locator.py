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

locator_login = LocatorLogin()