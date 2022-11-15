class B:
    def sy(self):
        pass


class A(B):
    def __init__(self):
        self.name = 'xky'


a = A()
print(dir(a))

print(eval("1 + 2"))  # 直接执行

frozenset('')  # 不可变类型

print(isinstance(a, A))  # 判断示例
print(isinstance(a, B))
# print(issubclass(B,a))


t = __import__('time')  # 可以直接导入字符串中的
print(dir(t))
print(t.ctime())
