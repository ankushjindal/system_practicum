from pylab import *
from scipy.io import wavfile
from numpy import arange

sampFreq, snd = wavfile.read('output.wav')
snd = snd / (2.**15)
s1 = snd[:,0]

timeArray = arange(0, 5060.0, 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000

plot(timeArray, s1[:len(timeArray)], color='k')
ylabel('Amplitude')
xlabel('Time (ms)')

show()
