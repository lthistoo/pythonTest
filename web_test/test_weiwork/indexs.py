#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 17:24
# @Author  : loubentai
# @File    : indexs.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web_test.test_weiwork.base_page import BasePage


class Indexs(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    """
    跳转到添加成员
    """
    def goto_add_member(self):

        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()

        return AddMember(self._driver)



    #
