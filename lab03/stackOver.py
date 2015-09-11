import time
from multiprocessing import Process, Manager


def test_f(test_d):
	"""  frist process to run
				exit this process when dictionary's 'QUIT' == True
	"""
	test_d['2'] = 2     ## change to test this
	while not test_d["QUIT"]:
		print("test_f", test_d["QUIT"])
		test_d["ctr"] += 1
		time.sleep(1.0)

def test_f2(name):
	""" second process to run.  Runs until the for loop exits
	"""
	for j in range(0, 10):
		print(name, j)
		time.sleep(0.5)

	print("second process finished")


if __name__ == '__main__':
	##--- create a dictionary via Manager
	manager = Manager()
	test_d = manager.dict()
	test_d["ctr"] = 0
	test_d["QUIT"] = False

	##---  start first process and send dictionary
	p = Process(target=test_f, args=(test_d,))
	p.start()

	##--- start second process
	p2 = Process(target=test_f2, args=('P2',))
	p2.start()

	##--- sleep 3 seconds and then change dictionary
	##     to exit first process
	time.sleep(3.0)
	print("\n terminate first process")
	test_d["QUIT"] = True
	print("test_d changed")
	print("data from first process", test_d)

	time.sleep(5.0)
	p.terminate()
	p2.terminate()
