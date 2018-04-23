#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/9 下午11:57

"""
3. 写3个正则表达式，完成下面三个例子：

1: 把字符串 2018-01-01 用正则转化成 01/01/2018
2: 实现一个函数，把 CamelCase 字符串 用正则转化成 camel_case
3: 在slack中，存在uid和id的对应关系，如下面的变量 ID_NAMES 。通过Slack的API能获取聊天记录，但是内容用的是uid，请用正则表达式re.
sub函数实现uid和id的转换：

"""
import re
date = "2018-01-03"
a = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', date)

assert a is not None


