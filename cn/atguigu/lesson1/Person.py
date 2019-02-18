"""
@author:Fcant
@description：类、属性封装、getset、继承练习
@date: 2019-02-18/0018 下午 13:33
"""


class Person:
    """

    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# 类继承时会将属性方法都继承，重写父类的属性和方法将覆盖父类的属性和方法
class Student(Person):

    def study(self):
        print("studying")
