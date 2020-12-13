'''
Description: 投资测试用例类
Author: sunwang
Date: 2020-10-12 22:02:37
LastEditTime: 2020-11-09 23:30:16
LastEditors: sunwang
'''



from com_func.basepath import testpath
import yaml
import pytest


class Test_invest():
    '''
    description: 网页投资用例类
    param : 
    return {type} 
    '''

    test_data = yaml.load(open(testpath.TestData, encoding="utf-8"), Loader=yaml.FullLoader)  # 测试数据
    success_test_data = test_data["test_invest_success_data"]  # 成功用例数据
    test_invest_failed_un100_data = test_data["test_invest_failed_un100_data"]  # 失败用例数据
    test_invest_failed_un10_data = test_data["test_invest_failed_un10_data"]  # 失败用例数据

    @pytest.mark.parametrize('kwargs', success_test_data)
    def test_invest_success(self, kwargs, inverst_setup_class, inverst_setup):
        '''{kwargs["title"]}'''
        # 接收和执行类级别前后置
        Test_invest.investpage, Test_invest.url, Test_invest.userpage = inverst_setup_class
        # 执行带入参用例级别前置
        inverst_setup(self.investpage, self.url)
        # 投资
        money_amount_b = float(self.investpage.get_tender_money())
        self.investpage.input_money(str(kwargs["money"]))
        self.investpage.tender_click()
        # 校验结果
        res_ele = self.investpage.get_success_windows_info()
        assert res_ele == kwargs["expected"]
        # 校验账户减少金额与投资金额
        self.investpage.get_success_windows_onclick()
        money_amount_e = float(self.userpage.get_user_amount())
        money_amount = money_amount_b - money_amount_e
        assert money_amount == kwargs["money"]

    @pytest.mark.parametrize('kwargs', test_invest_failed_un100_data)
    def test_invest_failed_un100(self, kwargs, inverst_setup):
        '''{kwargs["title"]}'''
        # 执行带入参用例级别前置
        inverst_setup(self.investpage, self.url)
        # 投资
        self.investpage.input_money(str(kwargs["money"]))
        self.investpage.tender_click()
        # 校验结果
        res_ele = self.investpage.get_error_windows_info()
        assert res_ele == kwargs["expected"]

    @pytest.mark.parametrize('kwargs', test_invest_failed_un10_data)
    def test_invest_failed_un10(self, kwargs, inverst_setup):
        '''{kwargs["title"]}'''
        # 执行带入参用例级别前置
        inverst_setup(self.investpage, self.url)
        # 投资
        self.investpage.input_money(str(kwargs["money"]))
        # 校验结果
        res_ele = self.investpage.tender_text()
        assert res_ele == kwargs["expected"]

