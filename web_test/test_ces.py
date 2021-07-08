#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 17:19
# @Author  : loubentai
# @File    : test_ces.py
from web_test.index import Index


class Test_ces(Index):


    def test_register(self):
        result = self.goto_register().register()
        assert result