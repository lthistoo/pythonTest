#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 11:32
# @Author  : loubentai
# @File    : base.py
import os

from selenium import webdriver


class  Base():

    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.phantomjs()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     self.driver.quit()
