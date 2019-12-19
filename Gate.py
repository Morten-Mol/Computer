from Transistor import Transistor

class Gate:
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

    # OR-gate made out of 2 transistors. The drain from both are
    # compared and 1 is parsed as the output if any one of them
    # are 1
    def OR(self):
        t1_OR = Transistor(1,self.iTop)
        t2_OR = Transistor(1,self.iBot)

        return max((t1_OR.drain,t2_OR.drain))

    # Inverter - Called with only 1 input i.e Gate(input,_)
    def NOT(self):
        t1_NOT = Transistor(1,self.iTop)
        # Simulate the situation where
        # the Input current of the ciruit
        # goes directly to output if 
        # t1_NOT is closed
        if t1_NOT.drain == 0:
            return 1
        else:
            # Power flows through t1_NOT
            # and does not stop before going through transister
            # See : //www.electronics-tutorials.ws/logic/logic_4.htmlass
            return 0

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
            return 1
        else:
            return 0

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

    def XOR(self):
        # XOR gate using 2 AND gates with single inverted inputs and 1 OR gate
        # See https://www.cs.bu.edu/~best/courses/modules/Transistors2Gates/

        # NOT operation on one of the AND gate inputs
        AND_1 = Gate(self.iTop, Gate(self.iBot).NOT()).AND()
        AND_2 = Gate(Gate(self.iTop).NOT(), self.iBot).AND()

        # Use output of both ANDs for input of OR
        return Gate(AND_1,AND_2).OR()

# Quick tests
if __name__ == '__main__':
    a = Gate(1,0).XOR()
    b = Gate(0,0).NOR()
    print(a,b)
