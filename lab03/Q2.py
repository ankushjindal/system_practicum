from multiprocessing import Process
import time

X, Y = 3, 2

def info(title):
	print(title)

def parent(x):
	child_process = Process(target=child,args=(Y,))
	child_process.start()
	
	time.sleep(x)
	info('Parent Process')

	child_process.join()

def child(y):
	time.sleep(y)
	info('Child Process')

if __name__ == '__main__':
	info('main line')
	
	parent_process = Process(target=parent, args=(X,))
	parent_process.start()
	parent_process.join()

