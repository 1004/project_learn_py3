# coding=utf-8
# !/usr/bin/python3

"""
数值类型
"""

age = 10  # 整形
print(type(age))

money = 10.9  # float
print(type(money))

ageNext = age + 1
print(ageNext)

other = age + money
print(type(other))

"""
字符串
"""

name = 'x'
print(type(name))
ok = "ok"
print(type(ok))

print("我是 'xky'")  # 双引号里面嵌套单引号
print('x' * 7)  # 字符串也可以乘

"""
列表类型
"""
list1 = [1, 3, 44]
print(list1[0])  # 索引取值

list1.insert(0, 5)  # 新增
print(list1[0])

list1.append(109)  # 追加
print(list1[len(list1) - 1])

list1.remove(5)  # 删除
print(list1[0])

print(list1.count(109))  # 值出现的数量

print(len(list1))  # 列表长度

print(list1.index(44))  # 值的索引

"""
字典类型
"""
map1 = {'name': "xky", 'age': 198}
print(map1['name'])  # 取值
print(map1['age'])
print(map1.keys())  # 取key
print(map1.values())  # 取value
map1.pop('name')  # 删除
print(len(map1))

"""
bool
"""

is_ok = True
is_failed = False

print(type(is_ok))
