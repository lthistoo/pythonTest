#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 16:54
# @Author  : loubentai
# @File    : test_demo.py
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import selenium

from selenium import webdriver


class TestDemo1():
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.maximize_window()
        # #隐式等待
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()


    def test_demo(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="card-header"]')))
        self.driver.find_element_by_link_text("测试方舟号").click()
        # self.driver.find_element_by_css_selector(".topic-29506 .title > a").click()
        # self.driver.get("https://www.baidu.com/")
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID,"su").click()
        # self.driver.get("http://sahitest.com/demo/clicks.htm")
        # element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        # element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        # element_dblclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        #
        # action = ActionChains(self.driver)
        # action.click(element_click)
        # action.context_click(element_rightclick)
        # action.double_click(element_dblclick)
        # sleep(3)
        # action.perform()

    def test_moveto(self):
        self.driver.get("http://www.baidu.com/")
        elc = self.driver.find_element_by_xpath('//*[@id="u1"]/span')

        action = ActionChains(self.driver)
        action.move_to_element(elc)

        action.perform()


    def test_dragdrog(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id('dragger')
        drop_ele = self.driver.find_element_by_xpath('/html/body/div[2]')

        action = ActionChains(self.driver)
        sleep(3)
        #将a元素拖拽到B元素
        action.drag_and_drop(drag_ele,drop_ele).perform()
        sleep(3)

        #点击元素并且不放,到B元素释放/松开   release 传入一个元素 会移动到该元素 松开鼠标， 不传元素 直接松开
        # action.click_and_hold().release().perform()
        #点击元素并且不放,移动到B元素,然后松开鼠标
        # action.click_and_hold().move_to_element().release().perform()
    #模拟键盘输入
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath('(//input[@type="textbox"])[1]')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(2)
        action.send_keys(Keys.SPACE).pause(3)
        action.send_keys("tom").pause(2)
        action.send_keys(Keys.BACK_SPACE).pause(2).perform()

    def test_touch(self):
        self.driver.get("http://www.baidu.com/")
        el = self.driver.find_element_by_id("kw")
        el.send_keys("selenium测试")
        ele_sousuo = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        action.tap(ele_sousuo)
        sleep(3)
        action.perform()
        #滑动到底部
        action.scroll_from_element(el,0,10000).perform()


