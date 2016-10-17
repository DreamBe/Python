#!/usr/bin/python3

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    """docstring for MyThread"""

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Thread Start:" + self.name)
        # 线程锁机制
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        threadLock.release()
        print("Thread Exit:" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
# thread1.join()
# thread2.join()
print("Exit with Main Thread")
