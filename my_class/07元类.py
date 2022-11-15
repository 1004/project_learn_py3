"""
元类：
    类也是一种对象，type 元类来创建类
    名称空间字典 = exec(类体字符串)
    People = type(类名,基类，名称空间字典)

    type: 内置元类

作用：
    动态创建类


自定义元类
    继承type


创建对象：
    空对象：__new__


如果想让对象加括号也可以继续调用，那么在对象所在类种加__call__ 【对象的元类的call,在调回到对象的_new__,__init__】

    def __call__(self)
        return xxx



"""

# class People(object):
#     def __init__(self, name):
#         self.name = name
#
#     def say(self):
#         print("hello")


class_name = 'People'
class_body = """
def __init__(self, name):
    self.name = name

def say(self):
        print("hello")
"""
class_dict = {}
exec(class_body, {}, class_dict)
print(class_dict)

p = type(class_name, (object,), class_dict)
print(p)

print("===========自定义元类==================")


# 自定义元类 Teacher ==> MyMeta(class_name,(),class_dict) 传进类对象，默认type
class MyMeta(type):
    # ②将空对象给到self ，然后调用__init__ ,对对象进行填充参数
    def __init__(self, x, y, z):
        print(x)  # 类名
        print(z)  # 基类
        print(y)  # 字典

    # ①空对象的调用位置  cls:当前类  ，后面是传递的参数
    def __new__(cls, *args, **kwargs):  # args: 参数元组 kwargs : 参数字典 参数聚合---> 参数打散用
        return super().__new__(cls, *args, **kwargs)  # type.__new__(xx) 另一种方式

    # 整体的一个组合 而是Teacher类的③和④
    def __call__(self, *args, **kwargs):
        print(self)  # self == MyMeta() == Teacher类  类调用方法，则是普通的方法，不是绑定方法
        t_obj = self.__new__(self, *args, **kwargs)  # 产生Teacher的空对象
        self.__init__(t_obj, *args, **kwargs)
        t_obj.xxx = 'xxx'  # 可以统一加属性
        return t_obj


class Teacher(metaclass=MyMeta):

    # ③
    def __init__(self, name):
        self.name = name
        print("构造函数")

    # ④
    def __new__(cls, *args, **kwargs):
        return object().__new__(cls)


"""
分析对象创建过程： 【创建过程都是从无到有】万事都是对象，只有有的对象才可以调用()

1. Teacher --> 先有Teacher类--->Teacher类由Teacher的元类实例出来：Teacher-->MyMeta() [MyMeta()--->MyMeta--->Type()]
2. Teacher() ---> 有了Teacher类后，加括号调用，则说明Teacher的元类对象MyMeta的__call__  [Teacher==MyMeta()]
3. Teacher的元类MyMeta 中的__call__  调用 Teacher类的__new__ 产生空对象 ，在调用Teacher的__init__为对象赋值，最后返回这个Teacher对象
4. Teacher()-->返回的Teacher对象 赋值给左边变量

"""
t = Teacher('xky')  # 调用MyMeta 创建Teacher空对象，然后传参丰富对象，最后由Teacher空对象 创建Teacher的实例
print(t)
print(t.name)
print(t.__dict__)
