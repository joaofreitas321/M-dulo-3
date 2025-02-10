x = 10

def FuncaoA():
    global x
    x = int(input("Introduza o numero"))
    print(x)

FuncaoA
print(x)