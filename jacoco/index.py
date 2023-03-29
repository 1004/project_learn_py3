if __name__ == '__main__':
    # print("xxx")
    # i = '13'
    # a = int(i)
    # b = 201*1.0 / 257
    # print(i)
    # print(b)
    # d = int(b * 100)
    # print(int(b * 100))
    # print("%s%s" % (str(int(b*100)), '%'))
    #
    git = 'git://gerrit.lianjia.com/mobile_android/newlink'
    git_strs = git.split('/')
    al = git_strs[len(git_strs)-1]
    print(git.find("/"))
    print(al)