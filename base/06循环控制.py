"""
循环控制
"""

"""
while

终止循环   break
继续下一次循环 continue  

while True:

else
    while 正常条件形式的结束，会在执行while结束后，执行， 如果while 被break 中断，则不会执行， else也是while的一个语句
"""

pwd = input("请输入密码：")
while pwd != '123456':
    pwd = input("重新输入密码：")
else:
    print("登录成功")

count1 = 1
count2 = 1
while count1 <= 9:
    count2 = 1
    while count2 <= count1:
        print(f"{count2}*{count1}={count1 * count2} ",end='')  # end 去掉默认的换行符 ，也可以自定义最后一个字符例如*
        count2 += 1
    count1 += 1
    print("\n")

"""
for 循环

for 变量名  in 可迭代对象

range 范围函数

for break else  和 while 一样
"""

for v in ['1', '2', '4']:
    print(v)

for k in {"k1": 111, "k2": 222}:
    print(f"{k}")

for i in range(1, 10):
    print(i)

for i in range(10):
    print(i)  # [0,10)

for i in range(1, 10, 2):  # 有步长
    print(i)
