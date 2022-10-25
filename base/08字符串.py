"""
字符串
"""

msg = "hello"
msg = str(12323)  # 可以转字符串
# msg[0] = "H"  # 不能改 不可变类型
print(msg)

# 字符串截取
sp = msg[0:2]
print(sp)

sp = msg[0:6:2]  # 切片 字符串截取  有步长
print(sp)

sp = msg[5:-1:-2]  # 反向字符串截取  有步长
print(sp)

sp1 = msg[:]  # copy 新字符串
sp2 = msg[::-1]  # 反转字符串

print("hello" in "hello world")
print("kkkk ".strip(" "))  # 不传也是默认去掉空格 ，传则去掉字符

# 特殊字符分隔字符串
msg2 = "hello world"
msg2s = msg2.split(" ")
print(msg2s)

print(msg2.upper())  # 大写
print(msg2.lower())

print(msg2.startswith("hello"))
print(msg2.endswith("world"))

print(",".join("war"))  # 进行分隔

print("hello".replace("e", "E"))  # 字符串替换
print("213233".isdigit())  # 字符串是否为纯数字

in_age = input("请输入成绩").strip()

if in_age.isdigit():  # 数字判断
    age = int(in_age)
    if age > 60:
        print("合格")
    else:
        print("不合格")
else:
    print("不要乱输入")

# find 寻找字符串 更方便
print("hello".find("h"))

# 编码/解码
print("圣诞快乐".encode("utf-8"))
print("圣诞快乐".encode("utf-8").decode("utf-8"))
