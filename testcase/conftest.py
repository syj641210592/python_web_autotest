'''
Description: pytest.fixture文件
Author: sunwang
Date: 2020-10-10 21:46:54
LastEditTime: 2020-11-08 23:15:07
LastEditors: sunwang
'''


from html_page.login_page import LoginPage
from html_page.home_page import HomePage
from html_page.invest_page import InverstPage
from html_page.user_page import UserPage
from com_func.confread import config
from selenium.webdriver import Edge 
import pytest

@pytest.fixture(scope='class')
def login_setup_class():
    '''登录测试类用例前后置'''
    driver = Edge(executable_path=config.get("ENV", "drive_path"))

    loginpage= LoginPage(driver)
    yield loginpage  # 分割前后置的 yeild之前是前置方法，yeild之后是后置
    driver.quit()

@pytest.fixture()
def login_setup():
    '''登录测试用例前后置'''
    def _login_setup(page):
        page.fresh()
    yield _login_setup  # 分割前后置的 yeild之前是前置方法，yeild之后是后置


@pytest.fixture(scope='class')
def inverst_setup_class():
    '''投资测试类用例前后置'''
    # 生成驱动
    driver = Edge(executable_path=config.get("ENV", "drive_path"))
    # 登录
    loginpage = LoginPage(driver)
    loginpage.login(config.get("PRESENT", "phone"), config.get("PRESENT", "pwd"))
    # 主页进入抢投标
    homepage = HomePage(driver)
    homepage.inverst()
    # 投标页面
    inverstpage = InverstPage(driver)
    # 用户页面
    userpage = UserPage(driver)
    yield inverstpage, userpage  # 分割前后置的 yeild之前是前置方法，yeild之后是后置
    inverstpage.quit_driver()


@pytest.fixture()
def login_setup():
    '''投资测试用例前后置'''
    def _login_setup(page):
        page.fresh()
    yield _login_setup  # 分割前后置的 yeild之前是前置方法，yeild之后是后置

