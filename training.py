'''
Author: your name
Date: 2020-09-18 22:48:01
LastEditTime: 2020-09-20 17:16:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python_web_autotest\training.py
'''

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


from selenium.webdriver import Edge
from com_func.confread import config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def training_12306(driver):
        '''
        description: 13206练习
        param {driver:浏览器对象} 
        '''
        try:
                driver.get(r'https://www.12306.cn/index/')
                driver.find_element(By.XPATH, r'//a[text()="往返" and @href="javascript:void(0)"]').click() # 点击往返
                ele_start = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'fromStationFanText'))) # 定位起始地输入框
                driver.execute_script('arguments[0].value="广州";', ele_start)

                ele_end = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'toStationFanText'))) # 定位起始地输入框
                driver.execute_script('arguments[0].value="福州";', ele_end)

                ele_start_date = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'go_date'))) # 定位起始地输入框
                driver.execute_script('arguments[0].readonly=false;arguments[0].value="2020-10-20";', ele_start_date)


                ele_start_end = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'from_date'))) # 定位起始地输入框
                driver.execute_script('arguments[0].readonly=false;arguments[0].value="2020-10-21";', ele_start_end)
        except Exception as e:
                print("完成12306web自动化操作失败 报错内容%s" % e)

def training_layui_slider(driver):
        '''
        description: layui练习
        param {driver:浏览器对象} 
        '''
        try:
                driver.maximize_window()
                driver.get(r'https://www.layui.com/demo/slider.html')
                ele_dot = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, r'//div[@id="slideTest2"]//div[@class="layui-slider-wrap-btn"]'))) # 定位起始地输入框
                actions = ActionChains(driver)
                actions.click_and_hold(ele_dot).move_by_offset(200, 0).release().perform()
        except Exception as e:
                print("完成layui滑块自动化操作失败 报错内容%s" % e)


def training_layui_form(driver):
        '''
        description: layui练习
        param {driver:浏览器对象} 
        '''
        try:
                driver.get(r'https://www.layui.com/demo/form.html')
                actions = ActionChains(driver)
                # 选择浙江省
                ele_select = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//input[@placeholder="请选择省"]'))).click() # 定位省选择框
                ele_select_provincea = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//dd[text()="浙江省"]'))) # 定位浙江省
                actions.move_to_element(ele_select_provincea).click(ele_select_provincea).perform()
                actions = ActionChains(driver)
                # 选择杭州市
                ele_select = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//input[@placeholder="请选择市"]'))).click() # 定位市选择框
                ele_select_city = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//dd[text()="杭州"]'))) # 定位杭州市
                actions.move_to_element(ele_select_city).click(ele_select_city).perform()
                actions = ActionChains(driver)
                # 选择西湖区
                ele_select = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//input[@placeholder="请选择县/区"]'))).click() # 定位县/区选择框
                ele_select_county = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, r'//label[text()="联动选择框"]/ancestor::div[1]//dd[text()="西湖区"]'))) # 定位西湖区
                actions.move_to_element(ele_select_county).click(ele_select_county).perform()
                actions = ActionChains(driver)
        except Exception as e:
                print("完成layui表单自动化操作失败 报错内容%s" % e)


driver = Edge(executable_path=config.get('ENV', 'drive_path'))
driver.maximize_window()
training_12306(driver)
training_layui_slider(driver)
training_layui_form(driver)

time.sleep(2)
driver.quit()

