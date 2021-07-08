#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 11:27
# @Author  : loubentai
# @File    : test_window.py
from time import sleep

from Test_demo.base import Base


class TestWindow(Base):

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys("username")
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('17600105272')

        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('login')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)