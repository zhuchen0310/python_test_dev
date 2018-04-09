#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/9 下午11:28
'''
写一个匹配IP地址的正则表达式
'''

import re
exp = re.compile(r"""^(?:(?:25[0-5] | 
                         2[0-4][0-9] |
                         [1]?[0-9][0-9]?)\.){3}
                       (?:(?:25[0-5] | 
                         2[0-4][0-9] |
                         [1]?[0-9][0-9]?)$)""", re.X)

assert exp.match('192.168.1.1') is not None
assert exp.match('8.8.8.8') is not None
assert exp.match('256.0.0.0') is None