"""
进程池：
    ProcessPoolExecutor:

进程池：
    ThreadPoolExecutor
    submit 提交异步方法
    submit的返回值获取，Feature 对象，feature对象的result() 获取方法的结果，但是获取结果中，会阻塞，等着获取
    shutdown(); 关闭线程池，并且阻塞着-等着线程池执行完毕
    submit().add_done_callback() ; 可以添加任务完成的回调

协程：
    gevent
    pip3 install gevent

"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

pool = ThreadPoolExecutor(5)  # 可以传递线程池容量 ，线程个数固定


def task(n):
    print(n)
    time.sleep(2)


if __name__ == '__main__':
    pool.submit(task, 1)  # 任务提交
    print("----end-----")
