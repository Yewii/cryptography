import os,time,random
from multiprocessing import Process,Queue

#售票员进程
def Conductor(q):
    for value in['1','2','3']:
        print('第%s次运行'%value)
        print('售票员关门')
        print('通知司机')
        q.put(value)
        print('售票员开门')
        # time.sleep(random.random())
        time.sleep(2)
    print('Process to Conductor: %s' % os.getpid())


#司机进程
def Driver(q):
    while True:
        value=q.get(True)
        print('司机开车')
        print('司机停车')
        print('通知售票员')
    print('Process to Driver: %s' % os.getpid())



if __name__=='__main__':
    #为父进程创建通讯Queue，并传递给各个子进程
    q=Queue()
    pCon=Process(target=Conductor,args=(q,))
    pDri=Process(target=Driver,args=(q,))

    #启动进程
    pCon.start()
    pDri.start()

    pCon.join()

    #进程是死循环，所以强制终止
    pDri.terminate()


