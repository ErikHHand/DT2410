import numpy as np
import math
import glob
import sys
from scipy.io import wavfile
#np.set_printoptions(threshold=sys.maxsize)

Fs, temp = wavfile.read("piano.wav")

#temp = temp / temp[np.argmax(temp)]

length = temp.shape[0]
print(np.argmax(temp))
print(temp[np.argmax(temp), 0])
print(temp[np.argmax(temp), 1])

L = np.zeros(length)
R = np.zeros(length)



#wavfile.write("anotherTest.wav", Fs, temp)
