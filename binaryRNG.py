from Transistor import Transistor
import numpy as np

def RNG(numberOfBits):
    bunch = []
    for x in range(numberOfBits):
        # 8-bit list
        rand = np.random.randint(2,size=2)
        bunch.append(Transistor(rand[0],rand[1]))

    rng = 0
    for i,bit in enumerate(bunch):
        if bit.drain == 1:
            rng += 2**i

    return rng
