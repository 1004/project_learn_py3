print("m2 开始导入")

x = 10


def get():
    print(f"m2--->get{x}")


def change():
    global x
    x = 20
