"""
@author:Fcant
@description：
@date: 2019-02-17/0017 下午 13:03
"""


'''
参数传输
'''


def sum(a, b):
    print(a + b)


# 位置传参
sum(1, 3)
# 关键字传参
sum(a=3, b=1)


def ex1(*args):
    print(args)


# *只能接受位置参数，不定长参数的参数
ex1(1, 2, 3)


def ex2(**kwargs):
    print(kwargs)


# **可以接受关键字参数的传输，关键字参数和位置参数混合传输
ex2(b=12, c=12, a=1)


def abs(a, b):
    return a * b


print(abs(1, 3))


'''
参数解包
'''
t = (1, 2)
sum(*t)
xt = {'b': 12, 'a': 1}
sum(**xt)