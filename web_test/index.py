#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 16:44
# @Author  : loubentai
# @File    : indexs.py
from time import sleep

from TestDemo.base import Base
from web_test.login import Login
from web_test.register import Register


class Index(Base):
    """
    首页po
    """

    def goto_register(self):
        """
        1.点击立即注册
        2.进入注册的po
        :return:
        """

        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_css_selector(".index_head_info_pCDownloadBtn").click()
        sleep(4)
        return Register(self.driver)

    def goto_login(self):
        """
        1.点击企业登录
        2.进入企业登录po
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_css_selector(".index_top_operation_loginBtn").click()
        return Login(self.driver)

    # def __init__(self):
    #     ""
    #     # self.driver = webdriver.Chrome()
