# Uma função que calcula a tabuada de um número que lhe é passado
def tabuada(n1):
    for i in range (1,11):
        r = i * n1
        print(f"{i} x {n1} = {r}")

tabuada(4)