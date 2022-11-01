"""
自定义迭代器 【生成器-->迭代器】
yield 可以多次返回

yield 可以暂停到方法的任意一个位置，然后进行取
"""


def fun1():
    print("第一次")
    yield 1
    print("第二次")
    yield 2
    print("第三次")
    yield 3
    print("第四次")
    yield 4
    print("最后了")


g = fun1()
print(g)

# a = g.__next__()
# print(a)
# a = g.__next__()
# print(a)
# a = g.__next__()
# print(a)
# a = g.__next__()
# print(a)
# a = g.__next__()
# print(a)

"""
yield 可以中间传值

yield 可以中断执行

等着投喂

这样等着另一个程序执行完成后，将结果返回给另一个程序
send()  传值投喂了
close()  关闭生成器,就不能投喂了

"""


def cat(name):
    print("开始执行了")
    while True:
        print("停止了")
        x = yield None
        print("开始了")
        print("%scat eat%s" % (name, x))


generator = cat("Tom")
generator.send(None)  # 等价 next(generator)

generator.send("猫粮")


def dot():
    print("开始dot")
    x = yield 111
    print("运行中...%s " % (x))
    yield 222


dotgenerator = dot()
res = dotgenerator.send(None)  # 遇到yield 停止，并且将111返回，【返回阻塞 停止】
print(res)
res = dotgenerator.send("xxxx")  # 将xxxx 给到x 并向下执行 遇到yield ，再次停止返回后面的 222
print(res)
