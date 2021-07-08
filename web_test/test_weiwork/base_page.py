#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 15:56
# @Author  : loubentai
# @File    : base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ""
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_options = Options()
            chrome_options.debugger_address = "127.0.0.1:9992"
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(6)
        else:
            self._driver = driver


        if self._base_url != "":
            self._driver.get(self._base_url)



    def find(self,by, locator):
        return self._driver.find_element(by, locator)


    #显示等待
    def wait_for_click(self):
        #
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable)
