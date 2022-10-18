"""
列表类型
"""

res = list('hlll')
print(res)
print(list({'k1': 99, 'k2': 23}))

# 内置方法
li = [1222, 'xky', 'wst']

print(li[0])

# 新增
li.append("other")
print(li)
li.insert(2, 'two')
print(li)

new_li = [1, 3, 4]
li.extend(new_li)  # 扩展一个列表
print(li)

# 删除
li.remove('other')
print(li)

del li[0]
print(li)

li.pop()  # 从栈顶删除，也可以传递索引，根据索引删除
print(li)

# 切片 copy行为
print(li[:2])
print(li[:])
print(li[::-1])  # 反转

# 循环获取
for x in li:
    print(x)

# 清空
li.clear()

# 反转
li.reverse()

li = [23, 4, 4, 5]
# 排序
li.sort(reverse=True)  # 只能针对数字
print(li)

"""
元组：不可变的类别，类似数组，里面的数据不能修改
按照索引存放，只能读，不用来写
"""
array = (1, 1.2, 'aa')
print(array, type(array))
print(array[0])

"""
字典类型
"""
map1 = {'k1': 231, 'k2': 233}
print(type(map1))
map2 = dict(x=2, y=4)
print(map2)

# 类型转换
print(dict([[12, 3], ((32, 3))]))
print({}.fromkeys(["a", "b"], None))

# 内置方法

map1['k1'] = 3233  # 修改
print(map1)
map1['kk'] = 333  # 不存在新增
print(map1)

print(len(map1))
print('k1' in map1)

# 删除
del map1['k1']
print(map1)

map1.pop('kk')  # 删除的同时，可以有返回值
print(map1)

# 循环
for i in map1:
    print(i, map1[i])

for k in map1.values():
    print(k)

for v in map1.keys():
    print(v)

map1.update({"k4": 999})
print(map1.get("k4"))  # 存在 获取值
print(map1.get("k5"))  # key 不存在 不报错

map1.setdefault("k4", "kkk")
print(map1.get("k4"))
