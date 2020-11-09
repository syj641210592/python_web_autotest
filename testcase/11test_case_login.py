'''
Description: 登录测试用例类
Author: sunwang
Date: 2020-09-26 06:20:47
LastEditTime: 2020-10-12 22:38:29
LastEditors: sunwang
'''



from com_func.basepath import testpath
from com_func.log import logger
import yaml
import pytest


class Test_login():
    '''
    description: 网页登录用例类
    param : 
    return {type} 
    '''
    test_data = yaml.load(open(testpath.TestData, encoding="utf-8"), Loader=yaml.FullLoader)["test_login_data"]

    @pytest.mark.parametrize('kwargs', test_data)
    def test_login(self, kwargs, login_setup_class, login_setup):
        '''{kwargs["title"]}'''
        # 接收和执行类级别前后置
        self.loginpage = login_setup_class
        # 执行带入参用例级别前置
        login_setup(self.loginpage)
        self.loginpage.login(kwargs['phone'], kwargs['pwd'])
        res_ele = self.loginpage.find_ele(pat=kwargs['xpath'],pat_params=kwargs['expected'])
        try:
            assert res_ele
        except Exception as e:
            logger.error(f"执行用例失败{kwargs['title']}失败", exc_info=True)
            raise AssertionError
    
    


