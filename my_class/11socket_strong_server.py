"""
增强版 socket, 可以发送任意长度的东西

"""
import socket
import subprocess
import struct
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
server.bind(('127.0.0.1', 8081))
server.listen(5)

while True:
    conn, address = server.accept()
    print(f"客户端链接成功:{address}")
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:
                break
            data_str = data.decode('utf-8')
            print("客户发来内容了:", data_str)
            result = subprocess.Popen(
                data_str,
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            success = result.stdout.read()
            failed = result.stderr.read()

            send_data_byte = success + failed  # 发送的数据部分

            header = {
                'total_size': len(send_data_byte),
                'md5': 2323323
            }
            header_str_byte = json.dumps(header).encode('utf-8')  # 发送的头部数据

            header_prefix_byte = struct.pack('i',len(header_str_byte))  # 固定的4个字节 存储header长度

            conn.send(header_prefix_byte)
            conn.send(header_str_byte)
            conn.send(send_data_byte)

        except Exception as e:
            print(e)
            break
    conn.close()

server.close()
