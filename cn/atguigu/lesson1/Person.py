"""
@author:Fcant
@description：类、属性封装、getset、继承练习
@date: 2019-02-18/0018 下午 13:33
"""


class Person:
    """
    类属性：直接在类中定义的属性是类属性
        类属性可以通过类或类的实例访问到
        但是类属性只能通过类对象来修改，无法通过实例对象修改
    """
    count = 0

    def __init__(self, name):
        """
        实例属性，通过实例对象添加的属性属于实例属性
            实例属性只能通过实例对象来访问和修改，类对象无法访问修改
        :param name:
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# 类继承时会将属性方法都继承，重写父类的属性和方法将覆盖父类的属性和方法
class Student(Person):

    def __init__(self, name):
        """
        super()继承父类的所有属性
        """
        self._name = name

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

    """
    静态方法：
        在类中使用@staticmethod来修饰的方法属于静态方法
        静态方法不需要指定任何的默认参数，静态方法可以通过类和实例去调用
        静态方法，基本上是一个和当前类无关的方法，它是一个保存到当前类中的函数
        静态方法一般都是一些工具方法，和当前类无关
    """
    @staticmethod
    def use():
        print("Use classRoom")

    """
    __str__()这个方法会在尝试将对象转换为字符串时调用
    它的作用可以用来指定对象转换为字符串的结果
    """
    def __str__(self):
        return 'Person.Name is {}'.format(self._name)


p = Person('cf')
print(p)
s = Student('cd')
print(s)

