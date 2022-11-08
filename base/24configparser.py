"""
读取配置

"""

import configparser

config = configparser.ConfigParser()
config.read('24_config.ini')

print(config.sections())

print(config.options('section1'))

print(config.items('section1'))

print(config.get('section1','user'))

print(config.getint('section1','age'))