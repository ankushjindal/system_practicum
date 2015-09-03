# color A
# autocomplete S
# man, help, comments A
# quit S
# file input shell A
# clear T
# arrow - history - char matching T

pwd = os.getcwd()

def cd(cmd):
	global pwd
	temp_pwd = pwd
	second = cmd[1]
	if second[0] == '/':
		pwd = '/'
		path_list = list(filter(None, second[1:].split('/')))
	elif second[0] == '~':
		pwd = os.path.expanduser("~")
		path_list = list(filter(None,second[1:].split('/')))
	else:
		path_list = list(filter(None,second.split('/')))
	cd_iterative(path_list)

def cd_iterative(path_list):
	global pwd
	for path in path_list:
		temp_pwd = pwd
		if path == '..':
			pwd = '/'.join(pwd.split('/')[:-1])
		else:
			if(pwd=='/'):
				pwd += path
			else:
				pwd += '/'+path
		try:
			if (pwd==''):
				pwd='/'
			try_the_directory = os.listdir(pwd)
		except FileNotFoundError:
			print('ERROR')
			pwd = temp_pwd
			break

def dir(cmd):
	global pwd
	try:
		second = cmd[1]
		temp_pwd = pwd
		cd(['cd',second])
		arr = os.listdir(pwd)
		print('dir of '+pwd)
		pwd = temp_pwd
	except:
		print('dir of '+pwd)
		arr = os.listdir(pwd)
	for x in arr:
		print(x)

def environ(cmd):
	arr = os.environ
	for k in arr:
		print(k, ": " ,arr[k])

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
