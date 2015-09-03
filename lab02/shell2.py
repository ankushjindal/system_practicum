import os

pwd = os.getcwd()

def cd(cmd):
	global pwd
	temp_pwd = pwd
	second = cmd[1]
	
	if second[0] == '/':
		pwd = '/'
		path_list = list(filter(None,second[1:].split('/')))
	elif second[0] == '~':
		pwd = os.path.expanduser("~")
		path_list = list(filter(None,second[1:].split('/')))
	else:
		path_list = list(filter(None,second.split('/')))

	print(path_list)
	for path in path_list:
		cd_relative(path)

def cd_relative(path):
	global pwd

	temp_pwd = pwd
	if path == '..':
		pwd = '/'.join(pwd.split('/')[:-1])
		print(pwd)
	else:
		pwd += '/' + path
	try:
		try_the_directory = os.listdir(pwd)
	except FileNotFoundError:
		print('ERROR')
		pwd = temp_pwd

def dir(cmd):
	arr = os.listdir(pwd)
	print()
	for x in arr:
		print(x)
	print()

def echo(cmd):
	"""echo <comment>​­ Display <comment>​on the display followed by a new line. 
	(Multiple spaces/tabs may be reduced to a single space). """
	comment = ''
	for x in cmd:
		if(x != '\t' and x != 'echo'):
			comment += x + ' '
	print(comment)

def pause(cmd):
	"""
	​Pause Operation of shell until ‘Enter ’ is pressed
	"""
	# while(True):
	input()
		# if (request[-1] == '\n'):
			# break

def environ(cmd):
	arr = os.environ
	for k in arr:
		print(k, ": " ,arr[k])



while True:
	cmd = input(pwd + '$ ').split()

	if cmd[0] == 'cd':
		cd(cmd)

	elif cmd[0] == 'dir' or cmd[0] == 'ls':
		dir(cmd)

	elif cmd[0] == 'environ' or cmd[0] == 'env' or cmd[0] == 'environment' or cmd[0] == 'envi':
		environ(cmd)
	
	elif cmd[0] == 'echo':
		echo(cmd)

	elif cmd[0] == 'pause':
		pause(cmd)

	elif cmd[0] == 'help':
		help(cmd)		

	elif cmd[0] == 'quit':
		quit(cmd)			
