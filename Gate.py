from Transistor import Transistor

class TransGate:
    # Class for logic gates that only use transistors to function

    # Any logic gate has a top-most input and a bottom-most input
    # The output is then the result of the logic operation
    def __init__(self,*args):
        # Since the NOT-gate only needs one input, we do variable
        # amount of args for the class constructor
        if len(args) == 2:
            self.iTop = args[0]
            self.iBot = args[1]
        else:
            self.iTop = args[0]

        self.output = 1e9 # Set to "inf" to be make it apperent
                          # if output is not changed during call

    # An AND-gate can simply be modelled as two tranistors in series
    # The drain of the t1 transistor is passed at the source for the
    # t2 transistor
    def AND(self):
        t1_AND = Transistor(1,self.iTop)
        t2_AND = Transistor(t1_AND.drain,self.iBot)

        return t2_AND.drain
        #self.output = t2_AND.drain

    # OR-gate made out of 2 transistors. The drain from both are
    # compared and 1 is parsed as the output if any one of them
    # are 1
    def OR(self):
        t1_OR = Transistor(1,self.iTop)
        t2_OR = Transistor(1,self.iBot)

        return max((t1_OR.drain,t2_OR.drain))
        #self.output = max((t1_OR.drain,t2_OR.drain))

    # Inverter - Called with only 1 input i.e Gate(input,_)
    def NOT(self):
        t1_NOT = Transistor(1,self.iTop)
        # Simulate the situation where
        # the Input current of the ciruit
        # goes directly to output if 
        # t1_NOT is closed
        if t1_NOT.drain == 0:
            return 1
            #self.output =  1
        else:
            # Power flows through t1_NOT
            # and does not stop before going through transister
            # See : //www.electronics-tutorials.ws/logic/logic_4.htmlass
            return 0
            #self.output = 0

    def NOR(self):

        def input_flow():
        # Simulate wire going to gate of transistor in logic gate
        # See http://hyperphysics.phy-astr.gsu.edu/hbase/Electronic/trangate.html#c5
             if self.iTop or self.iBot:
                return 1
             else:
                return 0

        t1_NOR = Transistor(1,input_flow())

        if t1_NOR.drain == 0:
            #self.output = 1
            return 1
        else:
            return 0
            #self.output = 0

    def NAND(self):

        # Simulating wire flow around transisters
        # Start with output = 1
        NAND_output = 1

        # Define transistors for gate
        t1_NAND = Transistor(1,self.iTop)
        t2_NAND = Transistor(t1_NAND.drain,self.iBot)

        if t2_NAND.drain == 1:
            NAND_output = 0

        return NAND_output
        #self.output = NAND_output

class SumGate:
    # Logic gates that use multiple transistor level gates to function

    def __init__(self,iTop,iBot):
        self.iTop = iTop
        self.iBot = iBot

    def XOR(self):
        # XOR gate using 2 AND gates with single inverted inputs and 1 OR gate
        # See https://www.cs.bu.edu/~best/courses/modules/Transistors2Gates/

        # NOT operation on bottom input of two AND gates
        #NOT_1 = TransGate(self.iBot)
        #NOT_1.NOT()
        #NOT_2 = TransGate(self.iTop)
        #NOT_2.NOT()

        #AND_1 = TransGate(self.iTop, NOT_1.output)
        #AND_1.AND()
        #AND_2 = TransGate(NOT_2.output, self.iBot)
        #AND_2.AND()

        AND_1 = TransGate(self.iTop, TransGate(self.iBot).NOT()).AND()
        AND_2 = TransGate(TransGate(self.iTop).NOT(), self.iBot).AND()

        # Use output of both ANDs for input of OR
        #OR_1 = TransGate(AND_1.output, AND_2.output)
        #OR_1.OR()

        #return OR_1.output
        return TransGate(AND_1,AND_2).OR()

# Quick tests
if __name__ == '__main__':
    a = SumGate(1,0).XOR()
    b = TransGate(0,0).NOR()
    print(a,b)
