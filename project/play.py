import math
import pyaudio
import base64
import zlib
import time
import sys

PyAudio = pyaudio.PyAudio
LENGTH = 0.05
BITRATE = 100000

MESSAGE = open(sys.argv[1]).read().encode("utf-8")
compressed_mesaage = zlib.compress(MESSAGE)
print(len(MESSAGE), len(compressed_mesaage))

p = PyAudio()

for FREQUENCY in [ord(chr(_))*500 for _ in compressed_mesaage]:
    print(FREQUENCY)
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        try:
            WAVEDATA = WAVEDATA+chr(int(math.cos(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
        except ZeroDivisionError:
            continue
    for x in range(RESTFRAMES): 
        WAVEDATA = WAVEDATA+chr(128)

    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), channels = 1, rate = BITRATE, output = True)
    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()
