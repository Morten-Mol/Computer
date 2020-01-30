from AddSubSingle import SingleBitAddSub

def AddSub(Binary_A, Binary_B, operation):

    # Addition or subtraction
    if operation is 'Add' or operation is 'add':
        K = 0
    elif operation is 'Sub' or operation is 'sub':
        K = 1

    # position in binary number - counter
    pos = 0

    # List to put sums of each bit into
    sumList = []

    # Iterate over binary number, from right to left
    # i.e. flip the lists
    Binary_A.reverse()
    Binary_B.reverse()

    for bitA, bitB in zip(Binary_A, Binary_B):

        if pos is 0:
            firstBitOp = SingleBitAddSub(K,K,bitA,bitB)
            sumList.append(firstBitOp.sum)
            prev_cIn = firstBitOp.cOut

        elif pos == (len(Binary_A)-1):
            lastBitOp = SingleBitAddSub(K,prev_cIn,bitA,bitB)
            sumList.append(lastBitOp.sum)
            cOut = lastBitOp.cOut

        else:
            bitOp = SingleBitAddSub(K,prev_cIn,bitA,bitB)
            sumList.append(bitOp.sum)
            prev_cIn = bitOp.cOut

        pos += 1

    return sumList,cOut

if __name__ == "__main__" :
    binA = [0,1,0]
    binB = [0,1,1]
    operation = 'sub' #### THIS DOES NOT WORK, ONLY ADD WORKS AS INTENDED

    ans,signedBit= AddSub(binA,binB,operation)
    print(ans)
    print(signedBit)
