"""
增强版 socket, 可以接收任意长度的东西

"""

import socket
import struct
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('101.42.223.101', 8250))

print("链接服务器成功")

while True:
    cmd = input("请输入cmd命令:").strip()
    if len(cmd) == 0:
        print("命令不能为空")
        continue
    if cmd == 'q':
        print("退出系统")
        break
    client.send(cmd.encode('utf-8'))

    header_prefix_length_byte = client.recv(4)  # 先接收4个字节 长度数据
    header_length = struct.unpack('i', header_prefix_length_byte)[0]
    # print(header_length)

    header_byte = client.recv(header_length)  # 在接收header长度
    header_str = header_byte.decode('utf-8')
    print(f"接收的Header:{header_str}")
    header = json.loads(header_str)

    total_size = header['total_size']
    current_size = 0
    current_data_byte = b''  # 默认空字节
    while True:
        if current_size == total_size:
            break
        res_data_byte = client.recv(1024)
        current_size += len(res_data_byte)
        current_data_byte += res_data_byte

    print(current_data_byte.decode('utf-8'))

client.close()  # 回收资源
