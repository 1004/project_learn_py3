"""
迭代器

迭代取值，遍历取值
基于上一次的结果给到下次遍历

迭代器对象 __next__()

可迭代对象  __iter__()

next() 内置函数

iter() 内置函数

"""

a1 = [1, 3, 4, 56]
a1Inter = a1.__iter__()
print(a1Inter.__next__())

while True:
    try:
        v = a1Inter.__next__()
        print(v)
    except StopIteration:
        break
