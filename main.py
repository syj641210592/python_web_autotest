from selenium.webdriver import Edge
from com_func.confread import config
from com_func.basepath import testpath
from selenium import webdriver
import time

# 浏览器(指定驱动路径)
brown = Edge(executable_path=testpath.WebDrive)
brown.implicitly_wait(20)
brown.get(config.get("URL", "url"))
element_kc = brown.find_element_by_xpath(r'//div[@id="js-searchbox"]//span[text()="课程"]')
element_kc.click()
element_search_input = brown.find_element_by_xpath(r'//input[@id="js_keyword"]')
element_search_input.send_keys("孙忘")
element_search_home = brown.find_element_by_xpath(r'//ul[@id="js-tab"]//h2[text()="主页"]')
element_kc2 = brown.find_element_by_xpath(r'//ul[@id="js-tab"]//h2[contains(.,"课程")]')

'//div[@id="js-searchbox"]//span[text()="课程"]'
'//input[@id="js_keyword"]''
'//ul[@id="js-tab"]//h2[contains(.,"主页")]'
'//ul[@id="js-tab"]//h2[contains(.,"课程")]'
'//ul[@id="js-tab"]//h2[contains(.,"老师")]'
'//ul[@id="js-tab"]//h2[contains(.,"关于我们")]'
'//div[@id="js-agency-nav"]/following-sibling::div//h3[contains(.,"软件测试之python")]'
'//div[@id="js-course-block"]//h4[contains(.,"软件测试自学")]/following-sibling::div//span[text()="免费"]'
'//div[@id="js-course-block"]//h4[contains(.,"软件测试自学")]/following-sibling::div//span[text()="免费"]'
'//div[@id="js-course-block"]//h4[contains(.,"软件测试自学")]/following-sibling::div//span[contains(.,"1663")]'