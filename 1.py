#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/9 下午11:12

'''
1. 写一个匹配URL的正则表达式
支持如 www.google.com、http://www.example/file.html https://douban.com/tag 等URL的匹配
'''

import re

exp = re.compile(r'''^(https?:\/\/)?
                     ([\da-z\.-]+)
                     \.([a-z\.]{2,6})
                     ([\/\w \.-]*)\/?$
                     ''', re.X)
assert exp.match('www.google.com') is not None
assert exp.match('http://www.example/file.html') is not None
assert exp.match('https://douban.com/tag') is not None