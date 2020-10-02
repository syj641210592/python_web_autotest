'''
Author: sunwang
Date: 2020-09-26 06:20:47
LastEditTime: 2020-10-02 09:37:45
LastEditors: sunwang
Description: web自动化
FilePath: \python_web_autotest\testcase\testcase_login.py
'''

from html_page.login_page import LoginPage
from com_func.basepath import testpath
from com_func.confread import config
from selenium.webdriver import Edge 
import unittest
import ddt
import yaml
import pytest



@pytest.fixture(autouse=True)
def case_setup():
    print("---测试用例执行的前置---")
    yield  # 分割前后置的 yeild之前是前置方法，yeild之后是后置
    print("---测试用例执行的后置---")




@ddt.ddt
class Test_login(unittest.TestCase):
    '''
    description: 网页登录用例类
    param : 
    return {type} 
    '''
    test_data = yaml.load(open(testpath.TestData, encoding="utf-8"), Loader=yaml.FullLoader)["test_data"]


    @classmethod
    def setUpClass(cls):
        driver = Edge(executable_path=config.get("ENV", "drive_path"))
        driver.maximize_window()
        driver.implicitly_wait(10)
        cls.loginpage= LoginPage(driver)

    def setUp(self):
        self.loginpage.fresh()
    

    @ddt.data(*test_data)
    @ddt.unpack
    def test_login(self, title, **kwargs):
        '''{title}'''
        self.loginpage.login(kwargs['phone'], kwargs['pwd'])
        res_ele = self.loginpage.find_ele(pat=kwargs['xpath'],pat_params=kwargs['expected'])
        self.assertTrue(res_ele)
    
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.loginpage.quit_driver()
    


