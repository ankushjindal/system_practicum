# color and graphics - columns, more, ...A
# autocomplete S
# man, help, comments A
# quit - Done
# file input shell A
# clear T - Done 
# arrow - history - char matching T

import os
import readline

class MyCompleter(object):  # Custom completer

	def __init__(self, options):
		self.options = sorted(options)

	def complete(self, text, state):
		if state == 0:  # on first trigger, build possible matches
			if text:  # cache matches (entries that start with entered text)
				self.matches = [s for s in self.options 
									if s and s.startswith(text)]
			else:  # no text entered, all matches possible
				self.matches = self.options[:]

		# return match indexed by state
		try: 
			return self.matches[state]
		except IndexError:
			return None


pwd = os.getcwd()

def cd(cmd):
	global pwd
	
	try:	
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
	except:
		print("Usage: 'cd <dir_name>'")

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
			print('Error: cd: ' + path + ' does not exist!')
			pwd = temp_pwd
			break

def dir(cmd):
	global pwd
	try:
		second = cmd[1]
		temp_pwd = pwd
		cd(['cd',second])
		arr = [x for x in os.listdir(pwd) if not x.startswith('.')]
		print('dir of '+pwd)
		pwd = temp_pwd
	except:
		print('dir of '+pwd)
		arr = [x for x in os.listdir(pwd) if not x.startswith('.')]
	for x in arr:
		print(x)

def environ(cmd):
	"""Prints the list of env variabls as <variable>: <value>. """
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
	"""​Pause Operation of shell until ‘Enter ’ is pressed"""
	input()

def clear(cmd):
	# os.system('clear')
	# print("\n" * 100 )
	# print(chr(27) + "[2J")
	print("\x1b[2J\x1b[H") 
	# The string is a series of ANSI escape codes. \x1b[ is a control sequence introducer (hex 0x1B). Code 2J clears the entire screen.
	# Code H sets the cursor position, and without arguments defaults to the top left corner.

options = ['cd', 'dir', 'ls', 'environ', 'env', 'echo', 'clear', 'pause', 'help', 'quit']
completer = MyCompleter(options)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

while True:
	
	cmd = input(pwd + '$ ')
	readline.add_history(cmd)
	cmd = cmd.split()

	if cmd[0] == 'cd':
		cd(cmd)
	elif cmd[0] == 'dir' or cmd[0] == 'ls':
		dir(cmd)
	elif cmd[0] == 'environ' or cmd[0] == 'env' or cmd[0] == 'environment' or cmd[0] == 'envi':
		environ(cmd)
	elif cmd[0] == 'echo':
		echo(cmd)
	elif cmd[0] == 'clear' or cmd[0] == 'cls' or cmd[0] == 'clr':
		clear(cmd)
	elif cmd[0] == 'pause':
		pause(cmd)
	elif cmd[0] == 'help':
		pass
	elif cmd[0] == 'quit' or cmd[0] == 'exit':
		quit("Adiós Amigo")

		