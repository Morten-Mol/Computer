from Transistor import Transistor

t1 = Transistor(0,0)

print(t1.drain)

t1.Source(1) 

print(t1.drain)

t1.Gate(1)

print(t1.drain)
