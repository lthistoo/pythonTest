#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 17:59
# @Author  : loubentai
# @File    : conftest.py
import os
from selenium import webdriver

import pytest



@pytest.fixture()
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