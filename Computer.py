from Gate import Gate

if __name__ == '__main__':
    print(Gate(0,0).AND())
    print(Gate(1,0).AND())
    print(Gate(1,1).AND())

    print(Gate(0,0).OR())
    print(Gate(1,0).OR())
    print(Gate(1,1).OR())
