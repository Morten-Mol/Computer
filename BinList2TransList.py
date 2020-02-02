from Transistor import Transistor

def Bin2Trans(binList):
    transList = []
    for binary in binList:
        if binary == 1:
            transList.append(Transistor(1,1))
        else:
            transList.append(Transistor(0,0))

    return transList

if __name__ == '__main__' :
    bL = [1,0,1,0]
    tL = Bin2Trans(bL)
    for T in tL:
        print(T.drain)
