import time


def print_current_time(func):
    print(time.time())
    print('This is current time')
    func()


def f1():
    print('This is f1')


def f2():
    print('This is f2')


print_current_time(f1)
print_current_time(f2)