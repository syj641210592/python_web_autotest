'''
Description: 基础页面功能
Author: sunwang
Date: 2020-09-29 22:28:30
LastEditTime: 2020-11-04 23:41:53
LastEditors: sunwang
'''
import os
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from com_func.log import logger
from com_func.basepath import testpath

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
            self.params = pat

            if pat_params != "":
                pat = pat % pat_params
                self.params = pat

            if type == "located":
                self.ele = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((getattr(By, method), pat)))
            elif type == "clickable":
                self.ele = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable((getattr(By, method), pat)))
            elif type == "selected":
                self.ele = WebDriverWait(self.driver, wait_time).until(EC.element_located_to_be_selected((getattr(By, method), pat)))
        except Exception as e:
            logger.error(f"查找页面元素{self.params}失败", exc_info=True)
            self.ele = ""
            raise e
        finally:
            return self.ele

    def send_keys(self, send_text):
        '''输入文本'''
        self.ele.clear()
        self.ele.send_keys(str(send_text))

    def get_ele_text(self):
        '''获取元素文本'''
        return self.ele.text

    def ele_click(self):
        '''点击元素'''
        try:
            self.ele.click()
        except Exception as e:
            logger.error(f"点击页面元素{self.params}失败", exc_info=True)
            self.ele = ""
            raise e

    def get_ele_attribute(self, attr, ele=""):
        '''获取元素属性'''
        if ele == "":
            ele = self.ele
        return ele.get_attribute(attr)

    def switch_to_windows_frame(self, frame="default"):
        '''切换页面frame'''
        if frame == "default":
            self.driver.switch_to.default_content()
        elif frame == "parent":
            self.driver.switch_to.parent_frame()
        else:
            self.driver.switch_to.frame(frame)

    def windows_handle(self, handle="handles"):
        '''切换窗口句柄'''
        if handle == "handle":
            return self.driver.current_window_handle()
        elif handle == "handles":    
            return self.driver.window_handles()
        else:
            self.driver.switch_to_window(handle)

    def save_screenshot(self, filename, path=""):
        '''页面截图'''
        # 时间戳
        date_desc = time.strftime(r"%Y-%m_%d-%h_%H_%M_%S")
        # 定义截图文件名
        filename = os.path.join(os.sep, testpath.ScreenShot, date_desc+filename+".png")
        # 截图
        self.driver.save_screenshot(filename)
        
    def quit_driver(self):
        self.driver.quit()
