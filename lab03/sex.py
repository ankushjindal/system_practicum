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

def sandwich_print(func, argument_tuple, format):
	# format like "WhatIAmDoingIs: %f AndILikeDoingIt."
	print format
	func(*argument_tuple)
	print format\

def shinny_print(func):
	def temp_wrap():
		info(func.__name__+': START')
		func()
		info(func.__name__+': END')
	return temp_wrap

def shinny_print1(func):
	def temp_wrap(arg1):
		info(func.__name__+': START')
		func(arg1)
		info(func.__name__+': END')
	return temp_wrap

#when function takes no argument
@shinny_print
def temp():
	print 'x'

#when function takes one argument
@shinny_print1
def temp1(x):
	print x
