class Transistor:
    """
    Transistor with attributes source and gate, which creates output drain
    """
    ### Initialize transisitor values when created first time
    def __init__(self,source,gate):
        self.source = source
        self.gate = gate
        self.drain = self.Output()

    ### Change exisiting input values and calc new drain val
    def Source(self,source):
        self.source = source
        self.drain = self.Output()

    def Gate(self,gate):
        self.gate = gate
        self.drain = self.Output()

    ### Check output
    def Output(self):
        if self.source * self.gate == 1:
            return 1
        else:
            return 0
