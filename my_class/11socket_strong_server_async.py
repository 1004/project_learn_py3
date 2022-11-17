"""
增强版 socket, 可以发送任意长度的东西

"""
import socketserver


class SocketHander(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print(self.request)
        print(self.client_address)


server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), SocketHander)
server.serve_forever()  # 分配线程 执行任务
