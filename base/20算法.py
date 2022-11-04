"""
二分法
/  浮点型除法
// 整形进行除法
"""

a1 = [1, 2, 3, 5, 6, 7, 8, 9, 10]

find = 10
print(len(a1) / 2)
print(len(a1) // 2)


def binary_search(myList, find_num):
    if (len(myList) == 0):
        print("没找到")
        return
    if (len(myList) == 1):
        if (myList[0] == find_num):
            print("找到了")
            return
        else:
            print("未找到")
            return

    mid_index = int(len(myList) / 2)
    print(mid_index)
    if myList[mid_index] > find_num:
        binary_search(myList[:mid_index], find_num)
    elif myList[mid_index] < find_num:
        binary_search(myList[mid_index:], find_num)
    else:
        print("找到了")


binary_search(a1, find)
