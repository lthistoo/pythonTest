
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 16:54
# @Author  : loubentai
# @File    : register.py
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver ):
        self.driver = driver
    def register(self):
        """
        输入内容
        点击下拉框
        :return:
        """
        self.driver.find_element_by_id("corp_name").send_keys("测试测试")
        return True
