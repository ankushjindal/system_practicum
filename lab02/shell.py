#! /usr/bin/env python3

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
import signal
import getpass

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
# The string is a series of ANSI escape codes. \x1b[ is a control sequence introducer (hex 0x1B). Code 2J clears the entire screen.
# Code H sets the cursor position, and without arguments defaults to the top left corner.
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

def pretty_columns(list_of_strings):
	import sys, struct, fcntl, termios
	s = struct.pack('HHHH', 0, 0, 0, 0)
	t = fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, s)
	term_size = struct.unpack('HHHH', t)
	col_width = max (len(word) for word in list_of_strings) + 2 #padding
	# print(col_width)
	possible_cols = int(term_size[1]/col_width)
	# print(possible_cols)
	matrix = to_matrix(list_of_strings,possible_cols)
	for row in matrix:
		print("".join(word.ljust(col_width) for word in row))

def to_matrix(l,n):
	return [l[i:i+n] for i in range(0, len(l), n)]
################

print(DEFAULT+CLEAR)
pwd = os.getcwd()

def cd(cmd):
	global pwd
	temp_pwd = pwd
	try:	
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
		except:
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
	print(CONTENT)
	pretty_columns(arr)
	print(DEFAULT)
	
def environ(cmd):
	"""Prints the list of env variabls as <variable>: <value>. """
	# arr = os.environ
	arr = globals()
	print(HEADERBG+'environment variables->'+DEFAULT)
	for k in arr:
		print(INPUT+BOLD+k+CONTENT+ ": "+str(arr[k])+DEFAULT)

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
	getpass.getpass("Termoinal Paused")
	# input()

def clear():
	# print(chr(27) + "[2J")
	# print "%c[2J" % (27)
	print(CLEAR) 

def help(cmd):
	clear()
	if(cmd=='cd'):
		print(BOLD+"cd"+CONTENT+"\tusage: "+UNDERLINE+"cmd PATH"+CONTENT+"\n\tWill change the dircetory to the given path. If the given path does not exists, it tries to go to "+UNDERLINE+"nearest path possible"+CONTENT+". The path could be absoulte or relative.\n\n"+DEFAULT)
	elif(cmd=='dir'):
		print(BOLD+"dir"+CONTENT+"\tusage: "+UNDERLINE+"dir [PATH]"+CONTENT+"\n\tWill list all the files of the path mentioned. If no path is mentioned it lists the file of the current directory\n\n"+DEFAULT)
	elif(cmd=='pwd'):
		print(BOLD+"pwd"+CONTENT+"\tusage: "+UNDERLINE+"pwd"+CONTENT+"\n\tWill return the current directory.\n\n"+DEFAULT)
	elif(cmd=='environ'):
		print(BOLD+"environ"+CONTENT+"\tusage: "+UNDERLINE+"environ"+CONTENT+"\n\tWill list all the defined environment variables of the terminal\n\n"+DEFAULT)
	elif(cmd=='echo'):
		print(BOLD+"echo"+CONTENT+"\tusage: "+UNDERLINE+"echo COMMENT"+CONTENT+"\n\tDisplay ​<comment> ​ on the display followed by a new line. ( Multiple spaces/tabs are reduced to a single space).\n\n"+DEFAULT)
	elif(cmd=='pause'):
		print(BOLD+"pause"+CONTENT+"\tusage: "+UNDERLINE+"pause"+CONTENT+"\n\tPause Operation of shell until 'Enter' is pressed.\n\n"+DEFAULT)
	elif(cmd=='help'):
		print(BOLD+"help"+CONTENT+"\tusage: "+UNDERLINE+"help"+CONTENT+"\n\tHelp for the complete shell and all the commands.\n\n"+DEFAULT)
	elif(cmd=='quit'):
		print(BOLD+"quit"+CONTENT+"\tusage: "+UNDERLINE+"quit"+CONTENT+"\n\tQuit the shell.\n\n"+DEFAULT)
	else:
		print(CONTENT+"Available commands- cd, dir, pwd, environ, echo, clr, pause, help, quit.\n\n"+BOLD+"cd"+CONTENT+"\tusage: "+UNDERLINE+"cmd PATH"+CONTENT+"\n\tWill change the dircetory to the given path. If the given path does not exists, it tries to go to "+UNDERLINE+"nearest path possible"+CONTENT+". The path could be absoulte or relative.\n\n"+BOLD+"dir"+CONTENT+"\tusage: "+UNDERLINE+"dir [PATH]"+CONTENT+"\n\tWill list all the files of the path mentioned. If no path is mentioned it lists the file of the current directory\n\n"+BOLD+"pwd"+CONTENT+"\tusage: "+UNDERLINE+"pwd"+CONTENT+"\n\tWill return the current directory.\n\n"+BOLD+"environ"+CONTENT+"\tusage: "+UNDERLINE+"environ"+CONTENT+"\n\tWill list all the defined environment variables of the terminal\n\n"+BOLD+"echo"+CONTENT+"\tusage: "+UNDERLINE+"echo COMMENT"+CONTENT+"\n\tDisplay ​<comment> ​ on the display followed by a new line. ( Multiple spaces/tabs are reduced to a single space).\n\n"+BOLD+"clr"+CONTENT+"\tusage: "+UNDERLINE+"clr"+CONTENT+"\n\tWill clear the screen.\n\n"+BOLD+"pause"+CONTENT+"\tusage: "+UNDERLINE+"pause"+CONTENT+"\n\tPause Operation of shell until 'Enter' is pressed.\n\n"+BOLD+"help"+CONTENT+"\tusage: "+UNDERLINE+"help"+CONTENT+"\n\tHelp for the complete shell and all the commands.\n\n"+BOLD+"quit"+CONTENT+"\tusage: "+UNDERLINE+"quit"+CONTENT+"\n\tQuit the shell.\n\n"+DEFAULT)

def main(cmd):

	if cmd[0] == 'cd':
		cd(cmd)
	elif cmd[0] == 'dir' or cmd[0] == 'ls':
		dir(cmd)
	elif cmd[0] == 'environ' or cmd[0] == 'env' or cmd[0] == 'environment' or cmd[0] == 'envi':
		environ(cmd)
		# print (globals())
	elif cmd[0] == 'echo':
		echo(cmd)
	elif cmd[0] == 'clear' or cmd[0] == 'cls' or cmd[0] == 'clr':
		clear()
	elif cmd[0] == 'pause':
		pause(cmd)
	elif cmd[0] == 'help':
		if (len(cmd)!=1):
			print(cmd[1])
			help(cmd[1])
		else:
			help('complete')
	elif cmd[0] == 'quit' or cmd[0] == 'exit':
		print(HEADERBG+"Adiós Amigo"+ENDC)
		os._exit(1)
	elif cmd[0] == 'pwd':
		print(pwd)
	else:
		print(FAILBG+"Error: <" + cmd[0] + "> not found!\nType help."+DEFAULT)


def hand(signum, frame):
	print('Ctrl+Z Interupt Ignored.\n')

if len(sys.argv) == 2:
	try:
		file_name = pwd + '/' +sys.argv[1]
		_file = open(file_name)

		for cmd in _file:
			# print("~~~~~~~~~")
			cmd = cmd.split()
			main(cmd)
		print(ENDC+'hi')

	except:
		print(FAILBG+"Error: <" + sys.argv[1] +"> does not exist!"+DEFAULT)

else:
	while True:
		try:
			# print(pwd)
			options = [x for x in os.listdir(pwd) if not x.startswith('.')]
			completer = MyCompleter(options)
			readline.set_completer(completer.complete)
			readline.parse_and_bind('tab: complete')
			signal.signal(signal.SIGTSTP, hand)
			print(DEFAULT)
			cmd = input(pwd + '$ '+INPUT)
			readline.add_history(cmd)
			try:
				cmd = cmd.split()
				main(cmd)
			except:
				continue
		except KeyboardInterrupt:
			print(HEADERBG+"Adiós Amigo"+ENDC)
			os._exit(1)


