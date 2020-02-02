from Transistor import Transistor
from BinList2TransList import Bin2Trans

def Bin2Dec(binBunch):
    binBunch = Bin2Trans(binBunch)
    # Convert binary number to decimal number 
    dec = 0

    # Flip to go from original right to original left
    binBunch.reverse()

    for i,bit in enumerate(binBunch):
       if i == len(binBunch)-1:
           # Take care of signed bit
           dec = dec * (-1)
       else:
           # Do a normal bit conversion
           dec += bit.drain * 2**i

    return dec
if __name__ == '__main__':
    A = [1,0,1,0]
    print(Bin2Dec(A))
