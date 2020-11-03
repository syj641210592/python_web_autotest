'''
Description: 基础页面功能
Author: sunwang
Date: 2020-09-29 22:28:30
LastEditTime: 2020-11-03 23:50:02
LastEditors: sunwang
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from com_func.log import logger


class BasePage(object):
    def __init__(self, driver: WebDriver):
        '''
        description:基础页面初始化 
        param : {
            driver:驱动,
            url:目标网址
        }
        '''
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
    def fresh(self, url=""):
        '''刷新网页'''
        self.driver.get(url)

    def find_ele(self, method="XPATH", pat="", pat_params="", type="located", wait_time=10):
        '''查找页面元素'''
        try:
            if pat_params != "":
                 pat = pat % pat_params
            if type == "located":
                self.ele = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((getattr(By, method), pat)))
        except Exception as e:
            logger.error(f"查找页面元素{pat_params}失败", exc_info=True)
            self.ele = ""
            raise e
        finally:
            return self.ele

    def send_keys(self, send_text):
        '''输入文本'''
        self.ele.clear()
        self.ele.send_keys(send_text)

    def get_ele_text(self):
        '''获取元素文本'''
        return self.ele.text

    def get_ele_attribute(self, class_name, ele=""):
        '''获取元素属性'''
        if ele == "":
            ele = self.ele
        return ele.get_attribute(class_name)

    def quit_driver(self):
        self.driver.quit()
