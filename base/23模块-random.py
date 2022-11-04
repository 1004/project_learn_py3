import random


def make_code(len):
    code = ''
    for i in range(0, len):
        int_code = str(random.randint(0, 9))
        char_code = chr(random.randint(65, 90))
        r_code = random.choice([int_code, char_code])
        code += r_code
    print(code)


if __name__ == '__main__':
    make_code(6)
