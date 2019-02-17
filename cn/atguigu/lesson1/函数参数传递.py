"""
@author:Fcant
@description：函数参数传递学习笔记
@date: 2019-02-17/0017 下午 13:03
"""

'''
参数传输
'''


def sum(a: int, b: int) -> int:
    """
    求两个数的和
    :param a: 第一个参数
    :param b: 第二个参数
    :return: None
    """
    global c  # 将一个局部变量声明为全局变量
    c = 10

    scope = locals()  # 获取函数内部的命名空间
    print(scope)

    global_scope = globals()  # 获取全局的命名空间
    print(global_scope)

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

# 获取全局命名空间
scope = locals()
print(scope)
