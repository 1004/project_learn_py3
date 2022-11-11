"""
property 装饰器

@property
def age():  方法当属性用，但是看着是调用属性，其实内部执行的是装饰前的方法


xxx.age === >  xxx.age()   二者等价
    ...
"""


class People:
    def __init__(self, name):
        self.__name = name

    @property   # 方法可以用属性的方式操作
    def name(self):
        return self.__name

    @name.setter
    def name(self, my_name):  # 名称必须是name
        self.__name = my_name

    @name.deleter
    def name(self):   # 名称必须是name
        print("不能删")


p1 = People('xky')
print(p1.name)  # 获取
p1.name = 'wst'
print(p1.name)
del p1.name
