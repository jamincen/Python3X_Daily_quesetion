"""
### 多线程
# 进程是程序执行的的最小单元，每个进程都有独立的内存空间
# 线程是进程的一个实体，是系统调用的最小单位
# 线程是轻量级的，没有独立内存空间，它寄存在进程的内存地址中

    线程的5中状态：
    1.新建状态
        当一个线程被创建，再启动线程之前它一直处于新建状态
    2.就绪状态
        线程被启动时，由于还没分配到cpu资源，该线程在等待另一个线程执行完
        （等待cpu服务），此时线程被称为就绪状态
    3.运行状态
        当处于就绪状态的线程被调用并获取cpu资源时，此时为运行状态
    4.阻塞状态
        一个正在执行的线程在某些情况下得以让出cpu资源，会终止自己的执行过程，
        这时被称为阻塞状态。阻塞被消除后是回到就绪状态，不是运行状态
    5.死亡状态
        线程被终止、销毁、或执行完毕则进入死亡状态。不可在重新启动

    阻塞状态有分为三种情况：等待阻塞、同步阻塞、其它阻塞

    当某个线程需啊哟独占共享资源时，必须先上锁，这样别的线程就无法在操作。
    当操作完一定要将锁打开，别的线程才可以操作数据。

    同步阻塞：线程请求锁定时进入同步阻塞，一旦获得锁右边卫运行状态

    等待阻塞：等待其它线程通知的状态，线程获得条件锁定后，调用“等待”将进入
              这个状态，一旦其它线程发出通知，线程将进入同步状态，再次竞争条件锁。

    其它阻塞：指线程sleep、join或则等待io时的阻塞

    创建两种多线程的方式：
    _thread.start_new_thread()     import _thread
    threading.Thread()             import threading
    
"""
import threading
num = 10000
# 定义锁
lock = threading.Lock()
def thread(name):
    global num
    while num > 0:

        # 加锁 一定要放在判断总量之前
        # 如果没有加锁就释放锁会导致报错
        lock.acquire()
        if num > 0:    
            num -= 1
            print('%s出售 1 张电影片 === 剩余 %d 张电影票' %(name, num))
            # 释放锁
            lock.release()
        else:
            lock.release()
        
# 三种售票途径
businesses = ['美团','淘票','糯米']
for i in businesses:
    # 创建线程
    t = threading.Thread(target=thread, args=(i,))
    # 启动线程
    t.start()



"""
    其它常用方法：
    1.threading.Rlock()
        Rlock允许在同一线程中被多次acquire，而Lock却不许这种情况。使用Rlock，
        acquire和release必须成对出现
    2.threading.Condition()
        高级锁，能调用内部锁对象对应的方法，wait方法、notify方法、notifyAll方法
    3.threading.Semaphore和BoundedSemaphore
        Semaphore:在内部管理着一个计数器，调用acquire()计数器-1，调用release()
        计数器+1，当计数器到0时，在调用acquire()就会阻塞，知道其它线程调用release()
    4.join()
        若果一个线程在执行过程中要调用另外一个线程，并且要等到其完成后才能接着执行
    5.isAlive
        等价于is_Alive(self),判断线程是否运行  True、False  t1.isAlive()
    6.Daemon
    7.name
        t1.setName('i am a thread')
        
"""
