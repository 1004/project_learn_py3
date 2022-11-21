"""
队列：

    正常的： 先进先出
    LifoQueue: 先进后出
    PriorityQueue： 优先级队列， 数字越小，优先级高

"""

from multiprocessing import Queue

q = Queue(3)
q.put(1)
q.put(2)
q.put(3)
print(q.full())

print(q.get())
print(q.get_nowait())
print(q.get())
print(q.empty())

if __name__ == '__main__':
    ...
