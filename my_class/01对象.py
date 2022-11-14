"""
对象  和 java差不多

区别：
1. py对象 是解释器的，拥有绑定关系
2. 在定义的时候加载类，形成类的名称空间，可以通过类名访问，就是普通空间访问
3. 如果是类的对象进行访问，则有绑定关系，方法中第一个参数就是当前对象self
4. 对象访问属性，先从对象找，找不动在去类种找
5. 类种定义了 通用的一些属性，如果改变类的属性，则所有对象中访问的都变化，是一份对象
6. 构造函数：__init(self)__

绑定给对象： 对象调用， 传参是对象
    def h(self)

绑定给类： 类调用, 传参是类
    @classmethod
    def classM(cls)

非绑定方法：
    @staticmethod
    def id():




"""


class Teacher:
    __inner = 'ok'  # 私有属性，只能内部访问, 如果非要访问  则Teacher._Teacher__inner
    tea_name = "默认老师"

    # 构造函数初始化变量
    def __init__(self, tea_name):
        self.tea_name = tea_name
        self.__inner2 = "内部初始化"  # 可以动态扩展内部隐藏属性

    def teach(self):
        print(f"我是老师{self.tea_name},开始讲课")

    def get_inner(self):  # get 方法 和 set 方法操作
        return self.__inner

    def set_inner(self, outer):
        self.__inner = outer

    # 类方法
    @classmethod
    def factory(cls):
        return cls('hello')

    @staticmethod
    def generate_id():
        import uuid
        return uuid.uuid4()


print("========对象通用-->类相关--start===========")
print(Teacher.__dict__)  # 所有的都存储到这里
print(Teacher.tea_name)  # 类种通用的值，已改全改
print(Teacher.teach)
Teacher.age = 11  # 可以在类种扩展

print(Teacher.generate_id())
t1 = Teacher.factory()

print("========对象通用-->类相关--end===========")

print("========对象相关--start===========")
t1 = Teacher("xky")  # 带有构造函数
t2 = Teacher("wst")
print(t1.__dict__)
print(t1.tea_name)
print(t1.teach)
print(t1.teach())
print(t1.age)  # 动态扩展 但是你点不进去
t1.age = 12  # 也可以在对象中扩展
print(t1.age)  # 动态扩展

print(t2.__dict__)
print(t2.tea_name)
print(t2.teach)  # 绑定方法 ，第一个参数默认为当前对象
print(t2.teach())

print("========对象相关--start===========")

"""

封装性： 不让别人动

隐藏属性
    私有属性:  __a  加__   
    私有函数： def __ip()
"""

# 报错
# print(t1.__inner)

# 访问类内部隐藏属性， 不推荐
print(t1._Teacher__inner)
