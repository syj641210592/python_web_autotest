'''
Description: 投资测试用例类
Author: sunwang
Date: 2020-10-12 22:02:37
LastEditTime: 2020-10-12 22:03:28
LastEditors: sunwang
'''



from com_func.basepath import testpath
from com_func.log import logger
import yaml
import pytest


class Test_invest():
    '''
    description: 网页投资用例类
    param : 
    return {type} 
    '''
    test_data = yaml.load(open(testpath.TestData, encoding="utf-8"), Loader=yaml.FullLoader)["test_invest_data"]

    @pytest.mark.parametrize('kwargs', test_data)
    def test_login(self, kwargs, home_setup_class, page_setup):
        '''{kwargs["title"]}'''
        # 接收和执行类级别前后置
        self.homepage = home_setup_class
        # 执行带入参用例级别前置
        page_setup(self.homepage)

    


