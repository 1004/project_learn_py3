"""
执行入口文件
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 准备导入项目根目录到 path 数组，这样就可以在这个path目录下导入任何模块和包

# 导入项目根目录 ATM
sys.path.append(BASE_DIR)

# 导入core  跨文件导入
from core.src import f1

if __name__ == '__main__':
    f1()
