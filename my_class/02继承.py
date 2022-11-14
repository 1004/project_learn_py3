"""
继承：
 可以多继承，但是少用，语义不清楚
 mro ： 可以看查找顺序
 super: 按照发起者  mro进行查找 属性和方法


访问父类的属性和方法 有2种   注意【父类查找不是看着的基础关系，而是以发起者的mro 顺序进行查找】
1. 类名.xxx(self,参数)  可以子类访问父类
2. super().xxx(参数)--->super(类名，self).xxx(参数)  也可以访问父类
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("from parent:%s" % self.name)


class Child1(Parent):
    def __init__(self, name, subName):
        Parent.__init__(self, name)
        self.sub_name = subName

    def say2(self):
        Parent.say(self)
        print("child1")


class Child2(Parent):
    def __init__(self, name, sub_name):
        Parent.__init__(self, name)
        self.sub_name = sub_name


# 多继承
class Child3(Child1, Child2):
    def __init__(self, name1, name2, name3):
        self.sub_name = name3
        Child1.__init__(self, name3, name1)
        Child2.__init__(self, name2, name3)


class Child4(Parent):
    def __init__(self, name1, name2):
        super(Child4, self).__init__(name1)  # py2 也实用 如果是
        self.name2 = name2

    def say(self):
        # super().say()  # 方式一
        super(Child4, self).say()  # 方式二


if __name__ == '__main__':
    c1 = Child1("child1", "sub")
    print(c1.__dict__)
    c1.say()
    print(Child1.mro())  # 可以看到属性查找顺序
    c3 = Child3('1', '2', '3')
    c4 = Child4('n1', 'n2')
    print(c4.__dict__)
    c4.say()
