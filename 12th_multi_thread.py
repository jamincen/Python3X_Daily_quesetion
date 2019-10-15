### 多线程

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
