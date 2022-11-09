"""
log 日志能力
"""
import logging
from logging import config, getLogger
from log import logconfig

config.dictConfig(logconfig.LOGGING_DIC)

# 可以获取日志输入模块

# mLog = getLogger('kkk')
# mLog.debug("我是 kkk ")

mConsole = getLogger("终端提示")
mConsole.debug("只中断提示")

mUserLog = getLogger("用户模块")
mUserLog.info("测试用户登录")

logging.debug('xxxx')  # 默认走默认的log 配置
