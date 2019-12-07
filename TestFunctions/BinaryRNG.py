from Transistor import Transistor
import matplotlib.pyplot as plt
import numpy.random as npr

def BinaryRNG(numberOfBits):
    """
    Random number generator using numberOfBits transistors to produce
    a random decimal number of maximum size 2^numberOfBits
    """
    bunch = []

    # Create list containg random binary number of length numberOfBits
    for x in range(numberOfBits):
        # Set source and gate of transistor randomly
        rand = npr.randint(2,size=2)
        bunch.append(Transistor(rand[0],rand[1]))

    # Convert binary number to decimal number 
    rng = 0
    for i,bit in enumerate(bunch):
        rng += bit.drain * 2**i

    return rng

def BinaryRNG_Test(bits,iterations):
    """
    Test of transistor class by doing a random binary number a certain number of times
    and looking at the distribution.

    Input: bits = Amount of transistors used to produce the random number
         : iterations = Amount of RNG iterations
    """
    numbers = []
    iterations = int(iterations)

    # Create list of length iterations and populate it with random numbers
    # generated via the BinaryRNG-function
    for x in range(iterations):
        numbers.append(BinaryRNG(bits))

    # Count occurences of each possible number using bits
    occurences = []
    for x in range(1+2**bits):
        occurences.append(numbers.count(x))

    # Plot distribution of numbers generated
    plt.figure(1)
    plt.plot(occurences,'r')
    plt.grid(True)
    plt.xlabel('%d-bit number generated' % bits)
    plt.ylabel('Number of occurences in %d iterations' % iterations)
    plt.title('%d-bit transistor based RNG' % bits)
    plt.show()
