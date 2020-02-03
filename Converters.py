from Transistor import Transistor

def Bin2Trans(binList):
    transList = []
    for binary in binList:
        if binary == 1:
            transList.append(Transistor(1,1))
        else:
            transList.append(Transistor(0,0))

    return transList

def Bin2Dec(binBunch):
    binBunch = Bin2Trans(binBunch)
    # Convert binary number to decimal number 
    dec = 0

    # Flip to go from original right to original left
    binBunch.reverse()

    for i,bit in enumerate(binBunch):
       if i == len(binBunch)-1 and bit.drain == 1:
           # Take care of signed bit
           dec = dec * (-1)
       elif i == len(binBunch)-1 and bit.drain == 0:
           # Signed-bit is 0, do nothing
           pass
       else:
           # Do a normal bit conversion
           dec += bit.drain * 2**i

    return dec

if __name__ == '__main__':
    A = [1,0,1,0]
    print(Bin2Dec(A))
