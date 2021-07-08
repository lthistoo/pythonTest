#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 16:59
# @Author  : loubentai
# @File    : test_login.py
import shelve

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC



class TestLogin():
    def setup(self):
        options = Options()
        #和浏览器打开的调试端口进行通信
        options.debugger_address = "127.0.0.1:9992"
        self.driver = webdriver.Chrome(options=options)
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

    # def teardown(self):
    #     # self.driver.quit()

    def test_login(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("123")
        self.driver.find_element_by_css_selector('.custom-control-label').click()
        sleep(5)
        self.driver.get_cookies()
        # self.driver.find_element_by_css_selector('#user_remember_me').click()
        # WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(By.ID ,"user_remember_me")).click()


        # self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(10)

        #将数据存储到
        db = shelve.open("cookies")
        cookies = []
        db["cookies"] = db
# css=.custom-control-label
