def Soma(x,y):
    t = x + y 
    print(id(x))
    x = 0
    print(id(x))
    y = 0
    return t

x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))
t = Soma(x,Soma(y,z))

print(t)