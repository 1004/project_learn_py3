"""
正则表达式

re ： 模块
"""

import re

print(re.findall("\w", 'abcklkj()))'))  # \w  单个字符 数字 下划线
print(re.findall("ab*", 'a ab abb abbb '))  # * 左侧字符[0-n] 次
print(re.findall("ab+", 'a ab abb abbb '))  # + 左侧字符[1-n] 次
print(re.findall("ab?", 'a ab abb abbb '))  # ? 左侧字符[0-1] 次

# {n,m} 左侧字符重复n-m次  不写则无限{n,} [n,无限]
print(re.findall("ab{2,4}", 'a ab abb abbb '))
print(re.findall('\d+', '123',re.DOTALL))  # 匹配后直接把数字抠出，继续匹配其他的字符串

# [] 匹配制定字符一个，选择
