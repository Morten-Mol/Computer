from Transistor import Transistor

class Gate:
    # Any logic gate has a top-most input and a bottom-most input
    # The output is then the result of the logic operation
    def __init__(self,iTop,iBot):
        self.iTop = iTop
        self.iBot = iBot

    # An AND-gate can simply be modelled as an transistor
    def AND(self):
        t1 = Transistor(1,self.iTop)
        t2 = Transistor(t1.drain,1)
        return t2.drain
