
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 16:50
# @Author  : loubentai
# @File    : login.py
from selenium.webdriver.remote.webdriver import WebDriver

from web_test.register import Register


class Login():
    """
    登录页面的po
    """
    def scan(self):
        """
        扫码二维码
        :return:
        """
        pass
    def goto_register(self):
        """
        1.点击企业注册
        2.进入注册po
        :return:
        """
        self.dirver.find_element_by_css_selector("login_registerBar_link").click()
        return Register(self.dirver)






    def __init__(self, driver:WebDriver):
        self.dirver = driver