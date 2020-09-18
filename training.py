from selenium.webdriver import Edge
from com_func.confread import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置浏览器
drive = Edge(executable_path=config.get('ENV', 'drive_path'))
# 设置隐性等待
drive.implicitly_wait(15)
# 访问网站
drive.get(r'https://mail.qq.com/')
# 切换iframe
drive.switch_to.frame('login_frame')
# 账户输入框
ele_user = drive.find_element(By.ID, 'u')
ele_user.send_keys('3247119728')
# 密码输入框
ele_pwd = drive.find_element(By.ID, 'p')
ele_pwd.send_keys('123456789')
# 登录
ele_login = drive.find_element(By.ID, 'login_button')
ele_login.click()
time.sleep(2)
# 切换iframe
drive.switch_to.frame('tcaptcha_iframe')
# 独立密码框
ele_pwd2 = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.ID, 'tcaptcha_drag_thumb'))
    )
ele_pwd2.click()

