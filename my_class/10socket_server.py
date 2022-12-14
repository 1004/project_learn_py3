import socket
import subprocess
from threading import Thread,current_thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 模块中的socket类创建对象

server_socket.bind(("127.0.0.1", 8080))  # 绑定服务器地址和端口

server_socket.listen(5)  # 监听的连接池最大数量，超过则断开异常

def Task(coon):
    while True:
        try:
            data = coon.recv(1024)  # 接受客户端的内容，如果没有内容，应该会阻塞等着，有了，则继续执行
            if len(data) == 0:
                break
            data_str = data.decode('utf-8')
            print("客户发来内容了:", data_str)
            result = subprocess.Popen(
                data_str,
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            # coon.send(f"我来自服务器:{data_str}".encode('utf-8'))  # 在发回去  都是字节
            success = result.stdout.read()
            failed = result.stderr.read()
            if len(success) != 0:
                coon.send(success)
            elif len(failed) != 0:
                coon.send(failed)
            else:
                coon.send(f"命令错误：{data_str}".encode('utf-8'))
        except Exception as e:
            print(e)
            break

    coon.close()  # 最后不用了，可以断开链接

while True:
    coon, client_addr = server_socket.accept()  # 等着客户端链接，如果没链接，则阻塞，有链接了继续执行
    print(f"客户端来了:{client_addr}")
    t = Thread(target=Task,args=(coon,))
    t.start()

server_socket.close()
