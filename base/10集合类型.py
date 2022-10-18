"""
集合类型
"""

# 定义
s = {1, 3, 3, 4, 5}
print(type(s))

s1 = set({'23', '2323'})

# 类型转换
s2 = set([23, 44, 55])

# 内置方法
f1 = {"k1", "k2", "k3"}
f2 = {"k3", "k4"}
print(f1 & f2)  # 取交集
print(f1 | f2)  # 取并集
print(f1 - f2)  # 取差集

for i in f1:
    print(i)

f1.remove("k1")  # 删除

f1.add("k5")
