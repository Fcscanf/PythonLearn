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

    """
    实例方法：
        在类中定义的方法，以self为第一个形参的方法都是实例方法
        实例方法调用时，Python会将调用对象作为self传入
        实例方法可以通过实例和类去调用
            当通过实例调用时，会自动将当前对象作为self传入
            当通过类调用时，不会自动传递self，此时需要在类中手动传入一个类对象给形参self
    """
    def study(self):
        print("studying")

    """
    类方法：
        在类内部使用@classmethod来修饰的方法属于类方法
        在类内部使用第一个参数是cls，也会被自动传递，cls就是当前的类对象
            类方法和实例方法的区别，实例方法的第一个参数是self，而类方法的第一个参数是cls
            类方法可以通过类去调用，也可以通过实例调用，没有区别
    """
    @classmethod
    def play(cls):
        print("Play baskboot")


