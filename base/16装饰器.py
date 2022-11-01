"""
装饰器：


1.开闭原则
    装饰器： 用来在不改动源代码的基础上，扩展能力，其实感觉有点像接口

"""

import time


# 方式1 但是调用方式变了
# def calTimeNoReturnWrapper(f, *args):  # 对index 没有返回值的函数的一种时间的统计
#     start = time.time()
#     f(*args)  # 逻辑解耦  回调形式
#     print(time.time() - start)
#
#
# def index(x, y):
#     time.sleep(1)
#     print(f"index:{x},{y}")
#
#
# calTimeNoReturnWrapper(index, 10, 20)


# 方式2 闭包, 对 原来的函数的一种能力增强 ， 类似于java 的动态代理
def indexWrapper(f):
    def calTimeNoReturnWrapper(*args, **kwargs):  # 对index 没有返回值的函数的一种时间的统计，args聚合普通的参数为元组， keargs 聚合k=v为字典
        start = time.time()
        res = f(*args, **kwargs)  # 逻辑解耦  回调形式, 参数打散
        print(time.time() - start)
        return res

    return calTimeNoReturnWrapper


def index(x, y):
    time.sleep(1)
    print(f"index:{x},{y}")


index = indexWrapper(index)
index(10, 30)
index(20, 30)


@indexWrapper
def home(x):
    print(x)


home("xxx")

"""
语法糖
@装饰器

多个的话：从下往上加载

执行顺序： 从上往下执行
"""


def deco1(f):
    def wrapper1(*args, **kwargs):
        print("wrapper1 执行")
        res = f(*args, **kwargs)
        print("wrapper1 完成")
        return res

    return wrapper1


def deco2(f):
    def wrapper2(*args, **kwargs):
        print("wrapper2 执行")
        res = f(*args, **kwargs)
        print("wrapper2 完成")
        return res

    return wrapper2


def outer(x):
    def deco3(f):
        def wrapper3(*args, **kwargs):
            print("wrapper3 执行")
            res = f(*args, **kwargs)
            print("wrapper3 完成")
            return res

        return wrapper3

    return deco3


@deco1  # homex[wrapper1] = deco1(wrappr2)
@deco2  # homex[wrapper2] = deco2(wrappr3)
@outer(10)  # 先执行outer(10) ==> @deco3 == > homex[wrapper3] = deco3(homex)
def homex():
    print("xxxx")


homex()
