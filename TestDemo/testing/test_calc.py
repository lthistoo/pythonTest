#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 17:20
# @Author  : loubentai
# @File    : test_calc.py
import pytest

import os, sys

import yaml

from Test_diyi.testing.steps.calc import Calculator

sys.path.append(os.getcwd())
import sys
print(sys.path)


with open("../pythoncode/calc.yaml",encoding='UTF-8') as f :
    datas =yaml.safe_load(f)
    myids = datas["add"].keys()
    mydatas = datas["add"].values()

def get_steps():
    with open("steps/calc_step.yml",encoding='UTF-8') as f :
        steps = yaml.safe_load(f)

    return steps

cal = Calculator()


@pytest.mark.parametrize("a, b, result", mydatas, ids=myids)
def test_steps1(a, b, result):
    steps1 = get_steps()
    for step in steps1:
            if 'add' == step:
                assert result == cal.add(a,b)
            elif 'div' == step:
                assert result == cal.div(a, b)
            elif 'sub' == step:
                assert result == cal.div(a, b)
            # elif 'sub' == step:
            #     try:
            #         assert result == cal.sub(a, b)
            #     except Exception as m:
            #         print(m)


        # elif 'div' == step:
        #     assert result == cal.div(a, b)
        # elif 'sub' == step:
        #     assert result == cal.sub(a, b)


class Test_cal:

    #加法
    # @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("datas/calc.yaml")))
    # @pytest.mark.parametrize("a, b, result", mydatas, ids=myids )
    # def test_add(self, a, b, result):
        # print(mydatas)
        # print(f'\na:{a}')
        # print(f'\nb:{b}')
        # print(f'\n运算结果={result}')
        # steps1(a, b, result)
        # try:
        #     steps(a, b, result)
        # except Exception as msg:
        #     print(f"异常 {msg}")
        # else:
        #     print(result == login.add(a,b))

    # 减法
    def test_sub(self, login):
        assert 2 == login.sub(2,1)

    #乘法
    def test_mult(self, login):
        assert 2 == login.cal.mult(2,1)

    #除法
    def test_div(self, login):
        assert 1 == login.div(1,1)



    # def test_assume(self):
    #     print("登录")
    #     pytest.assume(1 == 2)
    #     print("搜索")
    #     pytest.assume(2 == 2)
    #     print("搜索1")
    #     pytest.assume(3 == 2)
    #     print("搜索2")
