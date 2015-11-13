import os
proxyflag = ""
if os.sys("env | grep proxy"):
	proxyflag = "-E"
os.sys("sudo " + proxyflag + " apt-get install python-dev python3-dev libevent-dev python-numpy portaudio19-dev")
os.sys("sudo " + proxyflag + " pip3 install pylab pyaudio")