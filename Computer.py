import matplotlib.pyplot as plt
from binaryRNG import RNG
import numpy as np

def RNGtest():
    numbers = []
    bits = 8
    for x in range(1000):
        numbers.append(RNG(bits))


    plt.figure(1)
    plt.hist(numbers,bins=range(min(numbers),max(numbers)+10,10))
    plt.grid(True)
    #plt.show()

    print(numbers.count(0),numbers.count(255))

#Something is wrong with the amount of 0 values compared to 255 values
#It should be just as likely to get 0 as 255 (0 is all 8 bits being 0 and 255 is all 8 bits being 1)
RNGtest()
