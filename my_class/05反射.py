"""
反射：
4个核心方法
    1. getattr()
    2. setattr()
    3. hasattr()
    4. delteattr()

从对象中不通过反射，通过2者配合也可以获取
    1. obj.__dict__   可以获取属性字典
    2. dir(obj)  获取可以点出来的属性

"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"我的名字{self.name}")


p = People("xky", 18)
print(dir(p))
print(p.__dict__)  # 获取属性字典

print("=====")
print(hasattr(p, 'name'))
print(getattr(p, 'name'))
print(getattr(p, 'name1', None))
print(setattr(p, 'name', 'wst'))
print(getattr(p, 'name'))
print(delattr(p, 'name'))

print(p.__dict__)
