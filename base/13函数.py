"""
函数

def 函数名(参数):
    函数体
    return  值
"""


def func1():
    print("first")


func1()


def fun2(x, y):
    print(x, y)


fun2(19, 2)


def fun3():
    pass


fun3()

"""
参数，形式参数，
实参：实际参数
"""

"""
位置实参

必须传值：多一个不行，少一个不行
关键字传参： key=value 的形式

混合使用：前面必须是正常的，后面是关键字传参【不可以重复传值】
"""


def fun4(x, y):
    print(x, y)


# 关键字传参
fun4(x=3, y=3)
fun4(3, y=4)

"""
默认形参
def cun(x,y=4)  第二个参数就可传，可不传，规范不可以赋值可变类型

"""


def fun5(x, y=4):
    print(x, y)


fun5(4)
fun5(4, 4)
fun5(5, y=2)

"""
可变参数
*

**

"""


def fun6():
    ...


def fun7(x, y, *z):
    print(x, y, z)
    print(z[0])


fun7(1, 2, 3, 4, 5, 6)
"""
函数

def 函数名(参数):
    函数体
    return  值
"""


def func1():
    print("first")


func1()


def fun2(x, y):
    print(x, y)


fun2(19, 2)


def fun3():
    pass


fun3()

"""
参数，形式参数，
实参：实际参数
"""

"""
位置实参

必须传值：多一个不行，少一个不行
关键字传参： key=value 的形式

混合使用：前面必须是正常的，后面是关键字传参【不可以重复传值】
"""


def fun4(x, y):
    print(x, y)


# 关键字传参
fun4(x=3, y=3)
fun4(3, y=4)

"""
默认形参
def cun(x,y=4)  第二个参数就可传，可不传，规范不可以赋值可变类型

"""


def fun5(x, y=4):
    print(x, y)


fun5(4)
fun5(4, 4)
fun5(5, y=2)

"""
形参：
*形参名  元组  形参名可以是任何名称， 最好是args

**形参名  字典   最好是 kwargs 【实参 key=value 形式赋值】


实参：
实参中如果带星  ，则打散参数在传值
实参中如果带2星  ，则打散参数【key=value】形式在传值

命名关键字 传参 ，必须用key=value
"""


def fun6():
    ...


def fun7(x, y, *z):  # z 可变参数，聚合成元组
    print(x, y, z)
    print(z[0])


def fun8(**kwargs):  # kwargs 可变参数，k=v 聚合成字典
    pass


fun7(1, 2, 3, 4, 5, 6)

fun5(*[4, 4])  # 打散列表的内容 4，4
fun7(**{'x': 1, 'y': 2, 'k2': 2})  # x=1 ,y=2,k2=2 在传值

"""
"""
