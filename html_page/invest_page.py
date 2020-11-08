'''
Description: 投资page页面操作
Author: sunwang
Date: 2020-10-27 22:52:13
LastEditTime: 2020-10-27 22:55:10
LastEditors: sunwang
'''

from html_page.page_locator import locator_inverst
from html_page.base_page import BasePage
class InverstPage(BasePage):
    '''
    description: 投资页面封装
    '''
    def fresh(self):
        '''刷新网页'''
        super().fresh()

    def input_money(self, money):
        '''输入金额'''
        self.find_ele(*locator_inverst.money_input).send_keys(money)

    def tender_click(self):
        '''点击投资'''
        self.find_ele(*locator_inverst.tender_button).click()

    def tender_text(self):
        '''获取点击投资按钮上的文本提示'''
        self.find_ele(*locator_inverst.tender_button).text

    def get_tender_money(self):
        '''获取输入金额框内剩余可投标金额'''
        money = self.find_ele(*locator_inverst.tender_money).get_attribute("data-amount")
        # money = re.search(r".+?(\d+)元$", str(money)).group(1).replace(",","")
        return money

    def get_error_windows_info(self):
        '''获取投资失败提示窗口信息'''
        self.find_ele(*locator_inverst.error_windows).text

    def get_success_windows_info(self):
        '''获取投资成功提示窗口'''
        self.find_ele(*locator_inverst.success_windows)

    def get_success_windows_onclick(self):
        '''获取投资成功提示窗口'''
        self.find_ele(*locator_inverst.success_windows_onclick).click()
        