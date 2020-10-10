'''
Author: sunwang
Date: 2020-09-26 06:20:47
LastEditTime: 2020-10-10 23:12:19
LastEditors: sunwang
Description: web自动化
FilePath: \python_web_autotest\testcase\testcase_login.py
'''


from com_func.basepath import testpath
import yaml
import pytest


class Test_login():
    '''
    description: 网页登录用例类
    param : 
    return {type} 
    '''
    test_data = yaml.load(open(testpath.TestData, encoding="utf-8"), Loader=yaml.FullLoader)["test_data"]

    @pytest.mark.parametrize('kwargs', test_data)
    def test_login(self, kwargs, login_setup_class, login_setup):
        '''{kwargs["title"]}'''
        self.loginpage = login_setup_class
        login_setup(self.loginpage)
        self.loginpage.login(kwargs['phone'], kwargs['pwd'])
        res_ele = self.loginpage.find_ele(pat=kwargs['xpath'],pat_params=kwargs['expected'])
        assert res_ele
    
    


