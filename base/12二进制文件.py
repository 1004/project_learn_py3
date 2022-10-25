"""
二进制文件操作
rb,wb,ab

1.读写都是二进制文件
2.不需要指定编码格式，都是固定的格式bytes
3.可以针对所有文件


rt:
    for line in file:

    line = file.readLine()
    len(line) == 0


rb:
   buf =  file.read(1024)


wb
    file.wirteLines(list)  将列表的内容遍历写到文件

    file.flush()
    file.close()
    file.name
    file.readable()
    file.writeable()
"""

# with open('../assets/file/test1.zip',mode='rb') as f:
#     print(f.read())


# in_sourceName = input("请输入源文件路径：").strip()
# in_targetName = input("请输入目标文件路径：").strip()
#
# with open(r'{}'.format(in_sourceName), mode='rb') as source, \
#         open(r'{}'.format(in_targetName), mode='wb') as target:
#     while True:
#         buf = source.read(1024)
#         if len(buf) == 0:
#             break
#         target.write(buf)


"""
文件指针

file.seek(n,m)  移动字节指针,m :模式 0 是从头开始， 1 是当前的位置  2 是文件的末尾
file.tell()  文件指针的位置

"""
