"""
属性查找
    ： 对象--->类---> 父类

    对象 类 元类 都不是一个概念

        类属性：   属于类，所有对象都可以访问，一改全改
        对象属性： 属于对象，通过self 或者对象自己赋值，对象独有
"""


# 元类
class MyMeta(type):
    n = 20

    def __init__(self, x, y, z):
        super(MyMeta, self).__init__(x, y, z)
        self.n = 50


class People:
    # n = 30

    def __init__(self):
        ...


class Student(People, metaclass=MyMeta):
    n = 10  # 类属性

    def __init__(self):
        ...


s = Student()
# print(s.n)
print(Student.n)  # Student 类 是 元类对象创建 ，所以先找元类对象中，发现构造函数里为元类对象已经赋值，找到了，找不到在找类，父类
