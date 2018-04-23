#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/13 上午9:57

# def f1(n):
#     print n
#     k = 8
#     def f2(x):
#         print x, n
#         return x ** n + k
#     return f2
# def f(*args, **kwargs1):
#     def f1(fuc):
#         print '{}{}'.format(args, kwargs1)
#         def f2(*args, **kwargs):
#             print kwargs1.get('d'), kwargs1.get('c')
#             return fuc(*args, **kwargs)
#         return f2
#     return f1
#
# # a = f1(2)
# # print a(4)
# # import ipdb
# # ipdb.set_trace()
# @f(10, 11, 12, d=3432, c=3434)
# def f3(*args, **kwargs):
#     return '{}{}'.format(args, kwargs)
#
# print f3(1, 3, 5, a=1, b=2)



class A(object):

    def __init__(self, name):
        self.name = name

    def add(self):
        pass