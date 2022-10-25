# coding=utf-8

"""
接受输入
"""

mType = input("请输入类型: ")  # 将输入的类型都会存储到字符串, 不管你输入的是什么类型的内容
print("你输入的类型是:" + mType)

mAge = input("请输入年龄：")  # 将输入的类型都会存储到字符串, 不管你输入的是什么类型的内容
print(type(mAge))

"""
格式化输出
f"xxx{xx}"  // f 填充字符串变量
r"{}".format(xx)  // r 保证字符不被转义
"""

# 按照位置对应
res = "my name is %s  age is %s" % ("xky", 18)  # 普通数字
print(res)

res1 = "my name is %(name)s  age is %(age)s" % {"name": "xky", "age": 12}  # 字典
print(res1)

res2 = "内容%d" % 12  # 数字
print(res2)

res4 = "我的名字 {0}{0} 你那里 {1}{1}".format("xky", 12)  # 按照 重复取值
print(res4)

res5 = "我的名字 {name}{age}".format(name="xky", age=12)  # 按照 重复取值
print(res4)

res6 = f'我的名字是{res4}'  # f 的用法  3.5 之后
print(res6)
