"""
有参装饰器

"""


def deco(type):
    def outer(fun):
        def wraper(*args, **kwargs):
            userName = input("请输入用户名").strip()
            spwd = input("请输入密码").strip()
            if (type == 'file'):
                print('来源文件')
            elif (type == 'db'):
                print('来源数据库')
            else:
                print('来源其他')
            if (userName == "xky" and spwd == "123"):
                fun(*args, **kwargs)
            else:
                print("用户名或者密码错误")

        return wraper

    return outer


@deco('file')  # 语法糖，如果@后面是个语句，则先先执行，执行后的结构 给到@， @outer   然后根据index = outer(index) 去拿到新的函数
def home(x, y):
    print(f"进入首页->pwd={x},name={y}")


home('xky', '12')
