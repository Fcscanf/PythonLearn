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
