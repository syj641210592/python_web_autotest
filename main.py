from selenium.webdriver import Edge
from com_func.basepath import testpath
from selenium.webdriver.common.by import By
from selenium import webdriver

# 浏览器(指定驱动路径)
brown = Edge(executable_path=testpath.WebDrive)
# 设置隐性等待
brown.implicitly_wait(15)
# 访问网站
brown.get(r'https://www.ketangpai.com/User/login.html')
try:
    element_user = brown.find_element(By.XPATH, r'//div[@id="login"]//input[@type="text" and @name="account"]')
    element_user.send_keys("6412xxxxx@qq.com")
    element_pwd = brown.find_element(By.XPATH, r'//div[@id="login"]//input[@type="password" and @name="pass"]')
    element_pwd.send_keys("33xxxxxsun")
    element_login = brown.find_element(By.XPATH, r'//div[@class="padding-cont pt-login" ]/a[@href="javascript:;" and text()="登录"]')
    element_login.click()
finally:
    brown.quit()


from selenium.webdriver import Edge
from com_func.basepath import testpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Edge(executable_path=testpath.WebDrive)
driver.get(r'https://kf.qq.com/product/weixin.html')
try:
    element_plus = driver.find_element(By.XPATH, r'//i[@id="m_1453"]')
    element_plus.click()
    element_wx = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, r'//i[@id="m_1453"]/ancestor::a[text()="手机版微信"]//following-sibling::dl//a[text()="微信群"]'))
    )
    element_wx.click()
    element_wx_set = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, r'//div[@id="faqlist"]//a[text()="微信群创建及设置方法"]'))
    )
    element_wx_set.click()
finally:
    driver.quit()