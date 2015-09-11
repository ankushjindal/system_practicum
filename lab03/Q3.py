from multiprocessing import Process
import time,sys

X, Y = 3, 2

def info(title):
	print(title)

def recfunc(i,n):
	# print(i)

	if i ==0:
		print ("Process Parent:")
		# pass
	elif i ==1:
		print("Process Child:")
		print (nprimes(n))
	elif i ==2:
		print("Process Grand-Child:")		
		# print (nfib(n))
	elif i == 3:
		print("Process great Grand-Child:")
		# print (intersect_fib_primes(n))
	else:
		return
	process1 = Process(target=recfunc, args=(i+1,n,))
	process2 = Process(target=recfunc, args=(i+1,n,))
	
	process1.start()
	process2.start()
	process1.join()
	process2.join()

def nprimes(n):
	import pyprimes
	p_gen = pyprimes.primes_below(n)
	p_arr = []
	try:
		while True:
			p_arr.append(next(p_gen))
	except StopIteration:
		pass
	finally:
		del p_gen
	return p_arr

def nfib(n):
	f_arr = []
	a, b = 0, 1
	while b < n:
		f_arr.append(b)
		a, b = b, a+b
	return f_arr

def intersect(a1,a2):
	s2 = set(a2)
	return [val for val in a1 if val in s2]

def intersect_fib_primes(n):
	a1 = nprimes(n)
	a2 = nfib(n)
	return intersect(a1,a2)

if __name__ == '__main__':
	info('main line')
	
	i = 0
	if len(sys.argv) != 2:
		print ("Wrong Format")
	else:			
		n = int(sys.argv[1])
		# recfunc(i,n)
		print ("Here")
		parent_process = Process(target=recfunc, args=(i,n,))	
		parent_process.start()
		parent_process.join()

