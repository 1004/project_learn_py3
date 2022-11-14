"""
动态：
一种事务，多种形态

抽象
"""

import abc


class Animal:
    def say(self):
        print("动物的基础发声")


class Dog(Animal):
    def say(self):
        super(Dog, self).say()
        print("旺旺")


def sayH(animal):
    animal.say()


# 抽象类
class BaseA(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def hello(self):
        pass

    def hello2(self):
        print("hello")


class A(BaseA):

    def hello(self):
        print("hello")


sayH(Dog())

a = A()

