"""
计算运算符  + - * /
"""

print(1 + 1)

"""
赋值运算符
"""
age = 10
age += 1
print(age)

"""
链式赋值
"""
x = y = z = 10
print(id(x), id(y), id(z))

"""
交叉赋值
"""
m = 10
n = 20
m, n = n, m
print(m, n)

"""
解压赋值
"""
moneys = [111, 333, 444, 555]
m1, m2, m3, m4 = moneys  # 必须全部拿到，不能多 不能少
print(m1, m2, m3, m4)
m11, m22, *_ = moneys  # _来占位表示其他的数组，_ 废弃变量
print(m11, m22, _)
