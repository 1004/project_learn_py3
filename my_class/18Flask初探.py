"""
作为服务器
"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/index')
def index():
    print(request)
    return 'ok'


app.run()
