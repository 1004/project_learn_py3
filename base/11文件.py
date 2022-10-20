"""
文件
"""

# 打开文件
f = open("../assets/file/aaa.txt", mode='rt', encoding="utf-8")
print(type(f))
print(f)

# 读取文件
print(f.read())

# 回收资源 
f.close()

# 回收应用资源
del f

"""
with as 
上下文操作
省略赋值，和关闭文件的操作
\ 可以换行
"""

# with open("../assets/file/aaa.txt", encoding="utf-8") as f1:
#     print(f1.read())
#
# with open("../assets/file/bbb.txt", mode="wt",encoding="utf-8") as f1, \
#         open("../assets/file/aaa.txt") as f2:
#     # print(f1.read())
#     print(f2.read())
#     f1.write("哈哈哈")
#


# in_userName = input("输入用户名：").strip()
# in_pwd = input("输入密码：").strip()
#
# with open('../assets/file/pwd.txt', mode='rt', encoding='utf-8') as up:
#     username, pwd = up.readline().strip().split(":")
#     if in_userName == username and in_pwd == pwd:
#         print("登录成功")
#     else:
#         print("用户名或者密码错误")


"""
写模式
wt

写模式，如果文件不存在，则创建空文件，如果文件存在，则清空源文件，重新写入，同时指针移到第一个
"""

# 写模式，如果文件不存在，则创建空文件，如果文件存在，则清空源文件，重新写入，同时指针移到第一个
# with open('../assets/file/w_demo.txt',mode='wt',encoding='utf-8') as f:
#     ...
#

# with open('../assets/file/w_demo.txt',mode='wt',encoding='utf-8') as f:
#     f.write("了可接受的 ")


"""
追加模式
at  文件不存在，则创建空文件，如果文件存在，则后面继续追加
"""

# with open('../assets/file/w_demo.txt', mode='at', encoding='utf-8') as f:
#     f.write("kldsjflk")


"""
文件拷贝
"""

# with open('../assets/file/aaa.txt', mode='rt', encoding='utf-8') as source, \
#         open('../assets/file/target.txt', mode='at', encoding='utf-8') as target:
#     for line in source:
#         target.write(line)
