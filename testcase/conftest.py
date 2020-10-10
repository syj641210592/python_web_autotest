from html_page.login_page import LoginPage
from com_func.confread import config
from selenium.webdriver import Edge 
import pytest

@pytest.fixture(scope='class')
def login_setup_class():
    '''登录测试类用例前后置'''
    driver = Edge(executable_path=config.get("ENV", "drive_path"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    loginpage= LoginPage(driver)
    yield loginpage  # 分割前后置的 yeild之前是前置方法，yeild之后是后置
    loginpage.quit_driver()

@pytest.fixture()
def login_setup():
    '''登录测试用例前后置'''
    def _login_setup(loginpage):
        loginpage.fresh()
    yield _login_setup  # 分割前后置的 yeild之前是前置方法，yeild之后是后置