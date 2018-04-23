#! /usr/bin/python
# -*- coding:utf-8 -*-
# @zhuchen    : 2018/4/23 上午8:23
import time

def f1():
    sum = 0
    for i in range(10000):
        sum += 1

def f2():
    time.sleep(10)

f1()
f2()