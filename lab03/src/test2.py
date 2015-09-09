from multiprocessing import Process
import os
import webbrowser
import time

file_name  = "abcd.txt"
sleep_duration = 3
site = "http://goo.gl/3v6wUh"

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid() 

def file_edit(name):
    info('file_edit')
    with open(file_name, "ab+") as f:
        for line in f:
            line = line.replace(" ","\t")

# def sleep_fn(duration):
#     time.sleep(duration)

# def open_browser(site):
#     webbrowser.open(site)

def fork_bomb():
    info('Fork Bomb')
    while true:
        os.fork()

def fork_bomb2():
    info("Dummy Fork!")

if __name__ == '__main__':
    info('main line')
    p1 = Process(target=file_edit, args=(file_name,))
    p2 = Process(target=time.sleep,args=(sleep_duration,))
    hog1 = Process(target=webbrowser.open,args=(site,))
    hog2 = Process(target=fork_bomb2)
    
    p2.start()
    hog1.start()    
    hog2.start()
    p1.start()

    p1.join()
    p2.join()
    hog1.join()
    hog2.join()