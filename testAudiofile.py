import numpy as np
import math
import glob
import sys
from scipy.io import wavfile
#np.set_printoptions(threshold=sys.maxsize)

Fs, temp = wavfile.read("piano.wav")

#temp = temp / temp[np.argmax(temp)]

length = temp.shape[0]
print(length)

L = np.zeros(length)

#for i in range(length):
    #L[i] = temp[i]
print(temp / temp[np.argmax(temp)])

wavfile.write("anotherTest.wav", Fs, temp)
