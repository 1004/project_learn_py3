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
m11, m22, *_ = moneys  # _来占位表示其他的数组，_ 废弃变量代表其他 *代表多个  多个值给到变量 "_"

"""
逻辑运算
"""
color = "红"  # and or not
print(not 18 > 90)  # not>and>or
print(18 > 9 and 8 < 19)

"""
成员运算符
"""
print("e" in "hello")  # 是否在内部
print("111" in ["111", "222"])
print("key" in {"key": "value"})
print("key" not in {"key": "value"})

"""
身份运算符
"""
# is 判断id 地址是否一致，值可能一样，id 不一样


"""
流程控制if
"""
if color == '红':
    print("红色")

if 18 < 8:
    print("小于")
else:
    print("大于")

if 18 < 9:
    print("大")
elif 18 > 8:
    print("消息")
else:
    print("无")

score = input("请输入成绩: ")
score = int(score)
if score < 60:
    print("不及格")
elif score < 80:
    print("优秀")
else:
    print("牛逼")
