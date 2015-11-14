import os

proxyflag = ""
if os.sys("env | grep proxy")==0:
	proxyflag = "-E"

os.sys("sudo " + proxyflag + " apt-get install build-essential python-pip python-dev python3-dev libevent-dev python-all-dev python-scipy python-matplotlib python-numpy portaudio19-dev libatlas-base-dev gfortran multimedia-jack libpng-dev libjpeg-dev libfreetype6-dev")
os.sys("sudo " + proxyflag + " pip3 install scipy pyaudio ")
os.sys("sudo " + proxyflag + " pip3 install pylab")

# To start recording :P
"""
Listening requires:
You may need to change "pcm.front cards.pcm.front" to "pcm.front cards.pcm.default" in /usr/share/alsa/alsa.conf.
jack_control dps period 64
dbus-launch jack_control start


Try this from the command line:

pulseaudio --kill  
jack_control  start
Then when your done do this:

jack_control exit  
pulseaudio --start
And sometimes jack wont die, so then do

Get jackd's PID:

ps -aux | grep jackd  
kill -9 jacksPID

pulseaudio --kill
jack_control  start 



Redirecting ALSA to PulseAudio
Use the following settings in /etc/asound.conf (or $HOME/.asoundrc)
/usr/share/alsa/alsa.conf
pcm.pulse {
    type pulse
}

ctl.pulse {
    type pulse
}

pcm.!default {
    type pulse
}
ctl.!default {
    type pulse
}
Redirecting PulseAudio to JACK
Edit ~/.pulse/default.pa or create it if it doesn't exist and paste this into it:
load-module module-native-protocol-unix
load-module module-jack-sink channels=2
load-module module-jack-source channels=2
load-module module-null-sink
load-module module-stream-restore
load-module module-rescue-streams
load-module module-always-sink
load-module module-suspend-on-idle
set-default-sink jack_out
set-default-source jack_in
"""
