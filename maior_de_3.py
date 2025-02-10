"""
Função que devolve o maior de 3 números:
"""
def Maior(x1,x2,x3):
    if x1 > x2 and x1 >x3:
        return x1
    if x2 > x1 and x2 > x3:
        return x2
    return x3


print(Maior(10,15,20))