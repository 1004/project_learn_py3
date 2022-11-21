"""
线程：
Lock:
    普通互斥锁，可能会造成死锁s
RLock:
    重入锁， 有个计数器

信号量：
    sm = Semaphore(5) 到0 了，才会都就绪了

Event 事件
    event = Event()
    event.wait()  一个线程等着
    event.set()  通知可以不用等了，继续执行



"""
from threading import Thread, Lock, RLock

mutex = Lock()


def run1():
    mutex.acquire()
    print("互斥锁")
    mutex.release()


if __name__ == '__main__':
    t1 = Thread(target=run1)
    t2 = Thread(target=run1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main")
