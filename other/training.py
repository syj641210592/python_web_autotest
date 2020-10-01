'''
Description: 
Author: sunwang
Date: 2020-09-18 22:48:01
LastEditTime: 2020-09-30 23:20:44
LastEditors: sunwang
'''

# from selenium.webdriver import Edge
# from com_func.basepath import testpath
# from selenium.webdriver.common.by import By
# from selenium import webdriver

# # 浏览器(指定驱动路径)
# brown = Edge(executable_path=testpath.WebDrive)
# # 设置隐性等待
# brown.implicitly_wait(15)
# # 访问网站
# brown.get(r'https://www.ketangpai.com/User/login.html')
# try:
#     element_user = brown.find_element(By.XPATH, r'//div[@id="login"]//input[@type="text" and @name="account"]')
#     element_user.send_keys("6412xxxxx@qq.com")
#     element_pwd = brown.find_element(By.XPATH, r'//div[@id="login"]//input[@type="password" and @name="pass"]')
#     element_pwd.send_keys("33xxxxxsun")
#     element_login = brown.find_element(By.XPATH, r'//div[@class="padding-cont pt-login" ]/a[@href="javascript:;" and text()="登录"]')
#     element_login.click()
# finally:
#     brown.quit()


# from selenium.webdriver import Edge
# from com_func.basepath import testpath
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = Edge(executable_path=testpath.WebDrive)
# driver.get(r'https://kf.qq.com/product/weixin.html')
# try:
#     element_plus = driver.find_element(By.XPATH, r'//i[@id="m_1453"]')
#     element_plus.click()
#     element_wx = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, r'//i[@id="m_1453"]/ancestor::a[text()="手机版微信"]//following-sibling::dl//a[text()="微信群"]'))
#     )
#     element_wx.click()
#     element_wx_set = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, r'//div[@id="faqlist"]//a[text()="微信群创建及设置方法"]'))
#     )
#     element_wx_set.click()
# finally:
#     driver.quit()


# from selenium.webdriver import Edge
# from com_func.confread import config
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # 设置浏览器
# drive = Edge(executable_path=config.get('ENV', 'drive_path'))
# # 设置隐性等待
# drive.implicitly_wait(15)
# # 访问网站
# drive.get(r'https://mail.qq.com/')
# # 切换iframe
# drive.switch_to.frame('login_frame')
# # 账户输入框
# ele_user = drive.find_element(By.ID, 'u')
# ele_user.send_keys('3247119728')
# # 密码输入框
# ele_pwd = drive.find_element(By.ID, 'p')
# ele_pwd.send_keys('123456789')
# # 登录
# ele_login = drive.find_element(By.ID, 'login_button')
# ele_login.click()
# time.sleep(2)
# # 切换iframe
# drive.switch_to.frame('tcaptcha_iframe')
# # 独立密码框
# ele_pwd2 = WebDriverWait(drive, 10).until(
#         EC.presence_of_element_located((By.ID, 'tcaptcha_drag_thumb'))
#     )
# ele_pwd2.click()


# from selenium.webdriver import Edge
# from com_func.confread import config
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# def training_12306(driver):
#         '''
#         description: 13206练习
#         param {driver:浏览器对象} 
#         '''
#         try:
#                 driver.get(r'https://www.12306.cn/index/')
#                 driver.find_element(By.XPATH, r'//a[text()="往返" and @href="javascript:void(0)"]').click() # 点击往返
#                 ele_start = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.ID, 'fromStationFanText'))) # 定位起始地输入框
#                 driver.execute_script('arguments[0].value="广州";', ele_start)

#                 ele_end = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.ID, 'toStationFanText'))) # 定位起始地输入框
#                 driver.execute_script('arguments[0].value="福州";', ele_end)

#                 ele_start_date = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.ID, 'go_date'))) # 定位起始地输入框
#                 driver.execute_script('arguments[0].readonly=false;arguments[0].value="2020-10-20";', ele_start_date)


#                 ele_start_end = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.ID, 'from_date'))) # 定位起始地输入框
#                 driver.execute_script('arguments[0].readonly=false;arguments[0].value="2020-10-21";', ele_start_end)
#         except Exception as e:
#                 print("完成12306web自动化操作失败 报错内容%s" % e)

# def training_layui_slider(driver):
#         '''
#         description: layui练习
#         param {driver:浏览器对象} 
#         '''
#         try:
#                 driver.maximize_window()
#                 driver.get(r'https://www.layui.com/demo/slider.html')
#                 ele_dot = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, r'//div[@id="slideTest2"]//div[@class="layui-slider-wrap-btn"]'))) # 定位起始地输入框
#                 actions = ActionChains(driver)
#                 actions.click_and_hold(ele_dot).move_by_offset(200, 0).release().perform()
#         except Exception as e:
#                 print("完成layui滑块自动化操作失败 报错内容%s" % e)


# def training_layui_form(driver):
#         '''
#         description: layui练习
#         param {driver:浏览器对象} 
#         '''
#         try:
#                 driver.get(r'https://www.layui.com/demo/form.html')
#                 actions = ActionChains(driver)
#                 # 选择浙江省
#                 ele_select = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//input[@placeholder="请选择省"]'))).click() # 定位省选择框
#                 ele_select_provincea = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//dd[text()="浙江省"]'))) # 定位浙江省
#                 actions.move_to_element(ele_select_provincea).click(ele_select_provincea).perform()
#                 actions = ActionChains(driver)
#                 # 选择杭州市
#                 ele_select = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//input[@placeholder="请选择市"]'))).click() # 定位市选择框
#                 ele_select_city = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//dd[text()="杭州"]'))) # 定位杭州市
#                 actions.move_to_element(ele_select_city).click(ele_select_city).perform()
#                 actions = ActionChains(driver)
#                 # 选择西湖区
#                 ele_select = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//input[@placeholder="请选择县/区"]'))).click() # 定位县/区选择框
#                 ele_select_county = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//dd[text()="西湖区"]'))) # 定位西湖区
#                 actions.move_to_element(ele_select_county).click(ele_select_county).perform()
#                 actions = ActionChains(driver)
#         except Exception as e:
#                 print("完成layui表单自动化操作失败 报错内容%s" % e)


# driver = Edge(executable_path=config.get('ENV', 'drive_path'))
# driver.maximize_window()
# training_12306(driver)
# training_layui_slider(driver)
# training_layui_form(driver)

# time.sleep(2)
# driver.quit()

from base64 import decode
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com_func.confread import config
from pywinauto.keyboard import send_keys
import time


def training_12306(driver):
        driver.get(r'https://www.12306.cn/index/')
        ele = driver.find_element(By.ID, r'index_ads')
        ele.location_once_scrolled_into_view 
        # driver.execute_script("arguments[0].scrollIntoView()", ele)
        time.sleep(2)
        
def file_input(driver, *args):
        driver.get(r"https://www.layui.com/demo/upload.html")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, r'testList'))).click()
        time.sleep(1)
        file_path = f'{"{SPACE}".join(args)}'
        send_keys(file_path)
        # for file_path in args:

        #         # send_keys('"')
        #         send_keys(f'''{file_path}''')
        #         # send_keys('"')
        #         send_keys('{SPACE}')
        send_keys("~")
        time.sleep(5)

        
driver = Edge(executable_path=config.get('ENV', 'drive_path'))
driver.implicitly_wait(15)
driver.maximize_window()
training_12306(driver)
file_input(driver, r'"C:\工具资料\工具\使用说明.txt"', r'"C:\工具资料\工具\20151213204619_5Bath.jpeg"')
driver.quit()
