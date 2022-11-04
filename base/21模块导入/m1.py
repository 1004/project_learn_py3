print("m1 开始导入")

x = 10


def get():
    print(f"m1--->get{x}")


def change():
    global x
    x = 20


if __name__ == '__main__':  # 如果直接执行，则会执行下面的代码， 如果是作为模块导入，则不会执行 因为__name__ 内置属性不同
    get()
