#! /bin/bash python

# color and graphics - columns, more, ...A
# autocomplete S
# man, help, comments A
# quit S - Done
# file input shell A
# clear T - Done 
# arrow - history - char matching S - Done

import os
import sys
import readline

class MyCompleter(object):  # Custom completer
	def __init__(self, options):
		self.options = sorted(options)
	def _listdir(self, root):
		"List directory 'root' appending the path separator to subdirs."
		res = []
		for name in os.listdir(root):
			path = os.path.join(root, name)
			if os.path.isdir(path):
				name += os.sep
			res.append(name)
		return res
	def _complete_path(self, path=None):
		"Perform completion of filesystem path."
		if not path:
			return self._listdir('.')
		dirname, rest = os.path.split(path)
		tmp = dirname if dirname else '.'
		res = [os.path.join(dirname, p)
				for p in self._listdir(tmp) if p.startswith(rest)]
		# more than one match, or single match which does not exist (typo)
		if len(res) > 1 or not os.path.exists(path):
			return res
		# resolved to a single directory, so return list of files below it
		if os.path.isdir(path):
			return [os.path.join(path, p) for p in self._listdir(path)]
		# exact file match terminates this completion
		return [path + ' ']
	def complete_extra(self, args):
		"Completions for the 'extra' command."
		if not args:
			return self._complete_path('.')
		# treat the last arg as a path and complete it
		return self._complete_path(args[-1])
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

### GRAPHICS ###
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
BLACKBG='\033[40m'
CLEAR='\x1b[2J\x1b[H'
#tweak this to change the graphics and use this only
#don't, I repeat don't change the options in print commands
DEFAULT = ENDC+BLACKBG+OKBLUE+BOLD
FAILBG = ENDC+BLACKBG+FAIL
HEADERBG = ENDC+BLACKBG+HEADER+UNDERLINE
CONTENT = ENDC+BLACKBG+OKGREEN
INPUT = ENDC+BLACKBG
# class bg:
# 	red='\033[41m'
# 	green='\033[42m'
# 	orange='\033[43m'
# 	blue='\033[44m'
# 	purple='\033[45m'
# 	cyan='\033[46m'
# 	lightgrey='\033[47m'
# def green(s):
# 	return bcolors.OKGREEN+s+bcolors.ENDC
# def blue(s):
# 	return bcolors.OKBLUE+s+bcolors.ENDC
# def yellow(s):
# 	return bcolors.WARNING+s+bcolors.ENDC
# def violet(s):
# 	return bcolors.HEADER+s+bcolors.ENDC
# def red(s):
# 	return bcolors.FAIL+s+bcolors.ENDC
# def bold(s):
# 	return bcolors.BOLD+s+bcolors.ENDC
# def underline(s):
# 	return bcolors.UNDERLINE+s+bcolors.ENDC
################

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
		print(FAILBG+"Current directory:", pwd, "\nUsage: cd <dir_name>"+DEFAULT)

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
			print(FAILBG+'Error: cd: ' + path + ' does not exist!'+DEFAULT)
			pwd = temp_pwd
			break

def dir(cmd):
	global pwd
	try:
		second = cmd[1]
		temp_pwd = pwd
		cd(['cd',second])
		arr = [x for x in os.listdir(pwd) if not x.startswith('.')]
		print(HEADERBG+'dir of '+pwd+'->'+DEFAULT)
		pwd = temp_pwd
	except:
		print(HEADERBG+'dir of '+pwd+'->'+DEFAULT)
		arr = [x for x in os.listdir(pwd) if not x.startswith('.')]
	for x in arr:
		print(CONTENT+x+DEFAULT)

def environ(cmd):
	"""Prints the list of env variabls as <variable>: <value>. """
	arr = os.environ
	print(HEADERBG+'environment variables->'+DEFAULT)
	for k in arr:
		print(CONTENT+k, ": " ,arr[k]+DEFAULT)

def echo(cmd):
	"""echo <comment>​­ Display <comment>​on the display followed by a new line. 
	(Multiple spaces/tabs may be reduced to a single space). """
	comment = ''
	for x in cmd:
		if(x != '\t' and x != 'echo'):
			comment += x + ' '
	print(CONTENT+comment+DEFAULT)


def pause(cmd):
	"""​Pause Operation of shell until ‘Enter ’ is pressed"""
	input()

def clear(cmd):
	# os.system('clear')
	# print("\n" * 100 )	
	# print(chr(27) + "[2J")
	# print "%c[2J" % (27)
	print(CLEAR) 
	# The string is a series of ANSI escape codes. \x1b[ is a control sequence introducer (hex 0x1B). Code 2J clears the entire screen.
	# Code H sets the cursor position, and without arguments defaults to the top left corner.


options = ['cd', 'dir', 'ls', 'environ', 'env', 'echo', 'clear', 'pause', 'help', 'quit']
completer = MyCompleter(options)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

if len(sys.argv) == 2:
	try:
		file_name = pwd + '/' +sys.argv[1]
		_file = open(file_name)
	except:
		print(FAILBG+"Error: <" + sys.argv[1] +"> does not exist!"+DEFAULT)

while True:
	print(DEFAULT)
	cmd = input(pwd + '$ '+INPUT)
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
		print(HEADER+"Adiós Amigo"+ENDC)
		quit()		
	elif cmd[0] == 'pwd':
		print(CONTENT+pwd+DEFAULT)

		