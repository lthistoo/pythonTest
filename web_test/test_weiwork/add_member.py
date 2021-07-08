#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 17:26
# @Author  : loubentai
# @File    : add_member.py
from selenium.webdriver.common.by import By

from web_test.test_weiwork.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID, "username").send_keys("Mrlou1")
        self.find(By.ID, "memberAdd_acctid").send_keys("Mrlou123")
        self.find(By.ID, "memberAdd_phone").send_keys("17600101112")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
