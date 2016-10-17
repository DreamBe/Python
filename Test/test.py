#!/usr/bin/python3

import queue
import threading
import time

exitFlag = 1


class myThread (threading.Thread):

    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Start:" + self.name)
        process_data(self.name, self.q)
        print("End:" + self.name)


def process_data(threadName, q):
    while exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(5)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
# queueLock.acquire()
i = 0
for word in nameList:
    if workQueue.full():
        print("get:" + workQueue.get())
        workQueue.put(word)
        print("put: " + word)
    else:
        workQueue.put(word)
        print("put: " + word)
        i += 1
    print("i: %d q: %d" % (i, workQueue.qsize()))
# queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 0

# 等待所有线程完成
for t in threads:
    t.join()
print("Exit main thread")
