from random import randint

from time import time,sleep
from multiprocessing import Process
from os import getpid

def down(filename):
    print('启动下载，进程号{%d}.' % getpid() )
    print('开始下载%s...' % filename)
    time_to_down = randint(5,10)
    sleep(time_to_down)
    print('%s下载完成 消耗%d秒' % (filename,time_to_down))


def main():
    start = time()
    p1 = Process(target=down, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=down, args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()