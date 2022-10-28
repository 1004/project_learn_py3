"""
函数名 在栈中 属于变量 存储函数地址
函数  在堆中  属于对象
"""


def fun1(x, y, f):
    return f(x, y)


def fun2(x, y):
    return x + y


print(fun1(10, 10, fun2))
print(fun2)

"""
闭包

函数传参
"""


# 闭包函数
def fun3():
    x = 3

    def fun():
        print(x)  # 找定义阶段的变量

    return fun


fun = fun3()  # 可以将闭包函数 转为 全局函数

fun()


def fun4(x):
    def fun():
        print(x)

    return fun


bai = fun4('222')
bai()
