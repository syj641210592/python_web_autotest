'''
Description: 定位元素locator
Author: sunwang
Date: 2020-10-02 06:50:13
LastEditTime: 2020-10-29 21:44:45
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
        self.error_windows = ("XPATH", r'//div[@id="layui-layer1"]//div[@class="text-center"]')  # 投资失败弹窗
        self.success_windows = ("XPATH", r'//div[@id="layui-layer2"]//div[@class="capital_font1 note"]')  # 投资成功弹窗
        self.success_windows_onclick=("XPATH", r'//div[text()="投标成功！"]/..//button[text()="查看并激活"]')   # 投资成功弹窗查看并激活按钮
        
class LocatorUser(object):
    '''
    description:用户locator 
    param : 
    return {type} 
    '''
    def __init__(self):
        self.user_amount = ("XPATH", r'//li[@class="color_sub"]')  # 用户余额



locator_login = LocatorLogin()
locator_home = LocatorHome()
locator_inverst = LocatorInverst()
locator_user = LocatorUser()