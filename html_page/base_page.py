'''
Description: 基础页面功能
Author: sunwang
Date: 2020-09-29 22:28:30
LastEditTime: 2020-10-01 12:01:28
LastEditors: sunwang
'''
 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from com_func.log import logger


class BasePage(object):
    def __init__(self, driver, url, sleep_time):
        '''
        description:基础页面初始化 
        param : {
            driver:驱动,
            url:目标网址
        }
        '''
        self.driver = driver
        self.url = url
        self._open(sleep_time)
    
    def _open(self, sleep_time):
        '''初始化打开浏览器'''
        # 打开浏览器
        self.driver.get(self.url)
        self.driver.maximize_window()
        # 设置隐性等待
        self.driver.implicitly_wait(sleep_time)

    def fresh(self, url=""):
        '''刷新网页'''
        if url != "":
            self.driver.get(url)
        else:
            self.driver.get(self.url)

    def find_ele(self, method, pat, pat_params="", type="located", wait_time=5):
        '''查找页面元素'''
        try:
            if pat_params != "":
                 pat = pat % pat_params
            if type == "located":
                self.ele = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((getattr(By, method), pat)))
        except Exception as e:
            logger.error(f"查找页面元素{pat_params}失败", exc_info=True)
            self.ele = ""
        finally:
            return self.ele

    def send_keys(self, send_text):
        '''输入文本'''
        self.ele.clear()
        self.ele.send_keys(send_text)
