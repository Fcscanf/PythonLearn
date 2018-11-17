import time

'''
*args-可传多参数 **kw-关键字参数
'''
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator
def f1(func_time):
    print('This is f1 ' + func_time)


def f2(func_name1, func_name2, **kw):
    print('This is f1 ' + func_name1)
    print('This is f1 ' + func_name2)
    print(kw)


f = decorator(f1)
f('test_funtion')

f2('test_fun1', 'test_func2', a=1, b=2, c='1,2,3')
