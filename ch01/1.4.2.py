import random
import threading
import time


def thread_run(urls):
    for url in urls:
        time.sleep(random.random())
        print(url)


t1 = threading.Thread(target=thread_run, args=([1, 2, 3],))
t2 = threading.Thread(target=thread_run, args=([4, 5, 6],))
t1.start()
t2.start()


class MyThreading(threading.Thread):

    def __init__(self, name, urls):
        super().__init__(name=name)
        self.urls = urls

    def run(self):
        for url in self.urls:
            time.sleep(random.random())
            print(url)


m1 = MyThreading(name='m1', urls=[11, 12, 13])
m2 = MyThreading(name='m2', urls=[14, 15, 16])
m1.start()
m2.start()


class MyThreading1(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        global num
        while True:
            my_lock.acquire()
            if num > 104:
                my_lock.release()
                break
            num += 1
            my_lock.release()
            print(str(num))


my_lock = threading.RLock()
num = 100
m3 = MyThreading1(name='m3')
m4 = MyThreading1(name='m4')
m3.start()
m4.start()
'''
1. threading模块创建多线程

import random
import time, threading
# 新线程执行的代码:
def thread_run(urls):
    print 'Current %s is running...' % threading.current_thread().name
    for url in urls:
        print '%s ---->>> %s' % (threading.current_thread().name,url)
        time.sleep(random.random())
    print '%s ended.' % threading.current_thread().name

print '%s is running...' % threading.current_thread().name
t1 = threading.Thread(target=thread_run, name='Thread_1',args=(['url_1','url_2','url_3'],))
t2 = threading.Thread(target=thread_run, name='Thread_2',args=(['url_4','url_5','url_6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print '%s ended.' % threading.current_thread().name
'''
'''
通过从threading.Thread继承创建线程类的方式

import random
import threading
import time
class myThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls = urls

    def run(self):
    print 'Current %s is running...' % threading.current_thread().name
    for url in self.urls:
            print '%s ---->>> %s' % (threading.current_thread().name,url)
            time.sleep(random.random())
    print '%s ended.' % threading.current_thread().name
print '%s is running...' % threading.current_thread().name
t1 = myThread(name='Thread_1',urls=['url_1','url_2','url_3'])
t2 = myThread(name='Thread_2',urls=['url_4','url_5','url_6'])
t1.start()
t2.start()
t1.join()
t2.join()
print '%s ended.' % threading.current_thread().name

'''
'''
线程同步

import threading
mylock = threading.RLock()
num=0
class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self,name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print '%s locked, Number: %d'%(threading.current_thread().name, num)
            if num>=4:
                mylock.release()
                print '%s released, Number: %d'%(threading.current_thread().name, num)
                break
            num+=1
            print '%s released, Number: %d'%(threading.current_thread().name, num)
            mylock.release()


if __name__== '__main__':
    thread1 = myThread('Thread_1')
    thread2 = myThread('Thread_2')
    thread1.start()
    thread2.start()

'''

