from Transistor import Transistor

class Gate:
    # Any logic gate has a top-most input and a bottom-most input
    # The output is then the result of the logic operation
    def __init__(self,iTop,iBot):
        self.iTop = iTop
        self.iBot = iBot

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
