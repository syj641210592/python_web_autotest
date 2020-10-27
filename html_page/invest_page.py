'''
Description: 投资page页面操作
Author: sunwang
Date: 2020-10-27 22:52:13
LastEditTime: 2020-10-27 22:55:10
LastEditors: sunwang
'''

from html_page.page_locator import locator_inverst
from html_page.base_page import BasePage
import re
class InverstPage(BasePage):
    '''
    description: 投资页面封装
    '''

    def input_money(self, money):
        '''输入金额'''
        self.find_ele(*locator_inverst.money_input).send_keys(money)

    def tender_click(self, money):
        '''投资'''
        self.find_ele(*locator_inverst.tender_button).click()

    def get_tender_money(self, money):
        '''投标金额'''
        money = self.find_ele(*locator_inverst.tender_money).get_attribute("placeholder")
        money = re.search(r".+?(\d+)元$", str(money)).group(1).replace(",","")
        return money

        