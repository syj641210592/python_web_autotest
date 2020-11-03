'''
Description: 用户page页面操作
Author: sunwang
Date: 2020-10-29 22:17:15
LastEditTime: 2020-10-29 22:17:52
LastEditors: sunwang
'''


from html_page.page_locator import locator_user
from html_page.base_page import BasePage
import re
class UserPage(BasePage):
    '''
    description: 用户页面封装
    '''

    def get_user_amount(self):
        '''获取用户剩余金额'''
        user_amount = self.find_ele(*locator_user.user_amount)[:-1]
        return user_amount
        