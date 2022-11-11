"""
1. 内置名称空间
    系统的呗

2. 全局名称空间
    非函数 和类内的

3. 局部名称空间
    函数，my_class 内部的变量空间

加载顺序  内置>全局>局部
销毁顺序  内置<全局<局部
范围顺序  局部--> 全局-- > 内置

函数定义的时候，变量，定义为准
名字查找的关系，以定义为准
"""


def fun1():
    print(x)


x = 1


def fun2():
    x = 20
    fun1()


fun2()
print(x)  # 函数内部无法修改全局【上层】变量

"""
global nonlocal
global : 不可变类型 修改  则用 global
nonlocal : 不可变类型  修改外层的变量
"""


# 如何修改全局变量
def fun3():
    global x  # 告知使用全局的x,不用再造新值
    x = 33


print(x)
fun3()
print(x)
