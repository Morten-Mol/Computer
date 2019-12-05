from binaryRNG import RNG
import matplotlib.pyplot as plt

def RNGtest():
    numbers = []
    bits = 8
    for x in range(10000):
        numbers.append(RNG(bits))

    plt.figure(1)
    plt.hist(numbers,bins=range(min(numbers),max(numbers)+10,10))
    plt.grid(True)
    plt.xlabel('Random number generated')
    plt.ylabel('Number of occurences in set')
    plt.title("%d-bit transistor based RNG" % bits)
    plt.show()
