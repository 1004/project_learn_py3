"""
类似cmd执行命令
"""
import subprocess

obj = subprocess.Popen('ls /',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
res = obj.stdout.read()
print(res)
print(res.decode('utf-8'))


res_error = obj.stderr.read()
res_str = res_error.decode('utf-9')
print(res_str)