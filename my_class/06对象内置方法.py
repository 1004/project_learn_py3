"""
内置方法
    1. __str__   类似toString
    2. __delete__  销毁的时候自动调用，用来回收系统资源
"""


class Car:
    def __init__(self):
        self.name = 'TSL'

    def __str__(self):
        return "我是特斯拉"

    def __del__(self):
        print("回收系统资源")


c = Car()
print(c)
