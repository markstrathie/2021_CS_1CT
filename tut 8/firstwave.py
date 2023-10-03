import math
import wave

sampleRate = 44100   # hertz
duration = 1.0       # seconds
frequency = 440.0    # 440 hertz corresponds to note A

# initialize wave file
wavef = wave.open('sound.wav','wb')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2)
wavef.setframerate(sampleRate)

def generateNote( noteLetter, duration ):
    # generate signal and save to file
    for i in range(int(duration * sampleRate)):
        value = int(32767.0*math.cos(noteLetter*math.pi*i/sampleRate))
        data = value.to_bytes(2, 'little', signed=True)
        wavef.writeframesraw( data )

frequencies = {'c': 523.25, 
               'e': 659.25, 
               'f': 698.46, 
               'g': 783.99, 
               'a': 880.00}

bigben = [ "f","a","g","c","f","g","a","f","a","f","g","c","c","g","a","f" ]
for note in bigben:
    generateNote( frequencies[ (note) ], 1 )



# close wave file
wavef.writeframes(b'')
wavef.close()




