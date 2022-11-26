from wsgiref.simple_server import make_server


def run(env, response):
    response('200 OK', [])  # 响应首行 响应头
    print(env)
    return ["你好".encode('utf-8')]


if __name__ == '__main__':
    server = make_server(host='127.0.0.1', port=8083, app=run)
    server.serve_forever()
