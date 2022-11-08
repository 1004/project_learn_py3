"""
json 序列化

对象--->json.dumps()-->字符串
字符串---> json.load()---> 对象

json.dump()  可以将内容直接到保存文件

"""

import json

l = [1, 2, 3, 4]
print(json.dumps(l))

m = {"23": 234}
m_str = json.dumps(m)
print(m_str, type(m_str))

m_obj = json.loads(m_str)
print(m_obj, type(m_obj))

with open('my.json', mode='wt', encoding='utf-8') as f:
    json.dump(m, f)  # 等价 f.write(json.dump(m))
