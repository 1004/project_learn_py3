"""
队列：


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
