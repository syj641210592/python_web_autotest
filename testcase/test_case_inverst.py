'''
Description: 投资测试用例类
Author: sunwang
Date: 2020-10-12 22:02:37
LastEditTime: 2020-11-08 23:29:01
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
    def test_invest_success(self, kwargs, inverst_setup_class, login_setup):
        '''{kwargs["title"]}'''
        # 接收和执行类级别前后置
        self.investpage, self.userpage = inverst_setup_class
        # 执行带入参用例级别前置
        login_setup(self.investpage)
        # 投资
        money_amount_b = self.investpage.get_tender_money()
        self.investpage.input_money(kwargs["money"])
        self.investpage.tender_click()
        # 校验结果
        res_ele = self.investpage.get_success_windows_info()
        assert res_ele == kwargs["expected"]
        # 校验账户减少金额与投资金额
        self.investpage.get_success_windows_onclick()
        money_amount_e = self.userpage.get_user_amount()
        money_amount = money_amount_b - money_amount_b
        assert money_amount == kwargs["money"]

