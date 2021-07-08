#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 17:51
# @Author  : loubentai
# @File    : test_add_member.py
from web_test.test_weiwork.indexs import Indexs


class TestAddMember:
    def setup(self):
        self.index = Indexs()



    def test_add_member(self):
        self.index.goto_add_member().add_member()
