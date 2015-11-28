import io
import math
from pprint import pprint
from urllib.request import urlopen
import soundfile as sf

url = "http://tinyurl.com/shepard-risset"
data, fs = sf.read(io.BytesIO(urlopen(url).read()))

import sounddevice as sd
sd.play(data, fs)

fs, duration = 44100, 1.5
data = sd.rec(duration * fs, samplerate=fs, channels=2)

sf.write('file.mp3', data, fs)

fs = 44100/20
data = []
msg = 'Hello World!'
time_to_play = 0.5
time_of_char = int(fs*time_to_play/len(msg))

for char in msg:
    asci = ord(char)
    data.extend([[math.cos(_*asci), math.cos(_*asci)] for _ in range(time_of_char)])

sd.play(data, fs, blocking=False)
