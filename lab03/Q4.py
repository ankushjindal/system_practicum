from multiprocessing import Process, Manager
import time
import os
import psutil

X, Y = .001, .001

def info(title):
	print(title)

def child_1(test_d):
	info('C1: Start')
	x = "Shubham"

	ans = ""
	for i in x:
		ans += chr(ord(i)+10)
	print(ans)

	test_d["encrypt"] = ans
	info('C1: End')

def child_2():
	info('C2: Start')
	os.system("espeak < espeak")
	info('C2 : End')

def child_3():
	info('C3 : Start')

	file_old = open("espeak")
	file_new = open("espeak_new", "w+")
	for x in file_old:
		file_new.write(x)

	info('C3 : End')

def child_4(test_d):
	info('C4 : Start')
	
	cup_usage = psutil.cpu_times()
	print(cup_usage)
	test_d["cpu"] = cup_usage

	info('C4 : End')

def parent(x):
	c1 = Process(target=child_1,args=(test_d,))
	c2 = Process(target=child_2)
	c3 = Process(target=child_3)
	c4 = Process(target=child_4,args=(test_d,))
	
	c1.start()
	c2.start()
	c3.start()
	c4.start()
	
	time.sleep(x)
	info('Parent Process')

	c1.join()
	c2.join()
	c3.join()
	c4.join()

if __name__ == '__main__':
	info('main line')

	manager = Manager()
	test_d = manager.dict()
	test_d["encrypt"] = None
	test_d["cpu"] = None
	
	parent_process = Process(target=parent, args=(X,))
	parent_process.start()
	parent_process.join()

