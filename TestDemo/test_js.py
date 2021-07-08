#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 17:04
# @Author  : loubentai
# @File    : test_js.py
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep

from TestDemo.base import Base


class TestJS(Base):
    def test_js(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id('kw').send_keys("selenium")

        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath('//*[@id="page"]//a[last()]').click()
        sleep(2)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)

        for code in [
            'return document.title',
        ]:
            print(self.driver.execute_script(code))

    #修改时间控件
    def test_time(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script(" a=document.getElementById('train_date');a.removeAttribute('readonly'); a.value='2020-02-01'")
        sleep(6)
        print(self.driver.execute_script(" return document.getElementById('train_date').value"))

    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        sleep(3)
        #send_keys只能支持 input类型的文件上传  小心文件地址转义字符
        self.driver.find_element_by_id("stfile").send_keys("D:\Test_py\seleniumTest\Test_demo\img\pth.png")
        sleep(6)

    #弹窗处理
    def test_alert(self):

        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换进入表单
        self.driver.switch_to_frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")

        action = ActionChains(self.driver)
        #拖拽
        action.drag_and_drop(drag,drop).perform()

        self.driver.switch_to_alert().accept()
        sleep(4)
        self.driver.switch_to_default_content()
        sleep(3)
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)




