#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 16:04
# @Author  : loubentai
# @File    : conftest.py
from typing import List

import pytest

from Test_diyi.testing.steps.calc import Calculator


@pytest.fixture()
def login():
    cal = Calculator()
    print("开始计算")
    #生成器 能够激活fixture的 teardown方法     return 同时相当于暂停并记住上一次的执行位置
    yield  cal
    print("计算结束")



def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        print(item.nodeid)
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",    #注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )
    mygroup.addoption("--env1",    #注册一个命令行选项
                      default='sit',
                      dest='env1',
                      help='set your run env'
                      )

@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')
