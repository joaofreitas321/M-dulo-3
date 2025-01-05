"""
Elabore um programa que determine o quadrado de um nº inteiro n. O nº n deve ser
pedido ao utilizador e, através de uma função, devolver o seu quadrado.
"""

def calcular_quadrado(n):
    return n ** 2


def main():
    n = int(input("Introduza um número inteiro:"))
    quadrado = calcular_quadrado(n)
    print(f"O quadrado de {n} é {quadrado}.")



if __name__=='__main__':
    main()