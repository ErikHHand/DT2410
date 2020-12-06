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

left = np.zeros(length)
right = np.zeros(length)

for i in range(length):
    left[i] = temp[i, 0]
    right[i] = temp[i, 1]

left = left / abs(max(left.min(), left.max(), key=abs))
right = right / abs(max(right.min(), right.max(), key=abs))

# Write new aufio file
new_audio = np.zeros((left.shape[0], 2))

new_audio[:, 0] = left
new_audio[:, 1] = right

wavfile.write("anotherTest.wav", Fs, new_audio)
