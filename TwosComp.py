from Gate import Gate

def TwosComp(ini):
    number = ini

    comp = []

    for i, bit in enumerate(number):
        if i == len(number)-1 :
            comp.append(bit)
        else:
            comp.append(Gate(bit).NOT())

    return comp

if __name__ == '__main__' :
    A = [1,0,0]
    print(TwosComp(A))
