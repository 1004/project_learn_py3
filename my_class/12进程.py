"""
进程【并发】
1  一种直接创建
2  继承 Process 来自定义进程

进程：
    是一条执行程序的路
    从A进程 创建另一个进程B， 则可以说A 进程是B进程的父进程  A.join 则是挂载到B父进程上, 父进程就会阻塞，等着A 进程执行完


进程间通信
    通过公用一个Queue[JoinableQueue] 队列

"""

from multiprocessing import Process, current_process
import time
import os


def run_self(name):
    print("子进程")
    time.sleep(3)
    print('子进程结束', current_process().pid)
    print(os.getpid())
    print(os.getppid())


if __name__ == '__main__':
    p = Process(target=run_self, args=('xky',))
    # p.daemon= True  守护进程，父进程死了，子进程也会中断
    p.start()
    p.join()  # 主路是一个主进程 ，join 是将子进程挂载到主进程，这样，主进程[阻塞]必须等着挂着的进程执行后，执行
    p.is_alive()  # 进程是否存活\
    p.terminate()  # 中断进程
    print('主进程结束')
