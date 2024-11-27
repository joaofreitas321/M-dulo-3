"""
Programa que determine o quadrado de um nº inteiro n. O número n deve ser pedido
ao utilizador e, através de uma função, devolver o seu quadrado
"""
import math
def Quadrado(n1):
    return n1 ** 2

def main():
    n1 = int(input("Introduza um numero inteiro"))
    quadrado = Quadrado(n1)
    print(f"O quadrado de {n1} é {quadrado}")

if __name__=='__main__':
    main()