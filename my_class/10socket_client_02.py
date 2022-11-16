import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 客户端

client.connect(('127.0.0.1', 8080))  # 链接服务端 ,成功后继续执行，链接成功后，继续执行
print("客户端链接服务器成功...")
while True:
    content = input("请输入聊天内容:").strip()
    if len(content) == 0:
        print("输入内容不能为空")
        continue
    if content == 'q':
        print("退出聊天系统")
        break
    client.send(content.encode('utf-8'))  # 往服务器发送信息

    response = client.recv(1024)  # 也会阻塞，等着服务器的响应

    print("来自服务器的响应：", response.decode('utf-8'))  # 服务器的响应

client.close()  # 关闭连接
