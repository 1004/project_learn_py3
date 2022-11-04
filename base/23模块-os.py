import os

print(os.listdir('.'))
print(os.path.getsize('/Users/xiekongying/Desktop/xky/python/laonanhai/project_learn_py3/base/22包.py'))

# 执行某些命令逻辑【重要】
os.system('ls /')
os.system('pwd')

# 环境变量
print(os.environ)

print(os.path.basename('/a/b/c.txt'))  # 当前文件
print(os.path.dirname('/a/b/c.txt'))  # 当前目录
print(os.path.abspath(__file__))  # 绝对路径
print(os.path.split(__file__))  # 元组
print(os.path.isfile(__file__))  # 是否是文件
print(os.path.isdir(__file__))  # 是否是目录
