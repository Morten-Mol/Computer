from Gate import Gate

def TestGateTruth(gateType):
    """
    Creates truth table for given gateType

    Input: String - AND, OR etc.
    """

    # All possible inputs for the gates
    Inputs = [(0,0), (0,1), (1,0), (1,1)]


    print('---%s - Truthtable---' % gateType)

    # Iterate over all posible binary inputs
    for i in Inputs:
        TGate = Gate(i[0],i[1])

        if gateType == 'AND':
            output = TGate.AND()
            print('Input: %d, %d | Output: %d' % (i[0],i[1],output))

        if gateType == 'OR':
            output = TGate.OR()
            print('Input: %d, %d | Output: %d' % (i[0],i[1],output))

        if gateType == 'NOT':
            output = TGate.NOT()
            print('Input: %d, %d | Output: %d' % (i[0],i[1],output))

        if gateType == 'NAND':
            output = TGate.NAND()
            print('Input: %d, %d | Output: %d' % (i[0],i[1],output))

        if gateType == 'NOR':
            output = TGate.NOR()
            print('Input: %d, %d | Output: %d' % (i[0],i[1],output))

        if gateType == 'XOR':
            output = TGate.XOR()
            print('Input: %d, %d | Output: %d' % (i[0],i[1],output))

    # Spacer for next TestGateTruth call in Tests.py
    print('')
