import getopt
import sys
import os

# https://www.jianshu.com/p/b704f6c54d5a

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:", ['help', 'input='])
        print(opts, args)
    except getopt.GetoptError as e:
        print('error %s' % str(e))
