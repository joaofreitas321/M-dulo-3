"""
Programa que uma função receba como parâmetros de entrada as medidas dos dois catetos 
de um triângulo retângulo, e devolva a medida da hipotenusa.
"""
import math

def hipotenusa(cateto1,cateto2):
    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
    return hipotenusa

assert hipotenusa(4,3) == 5, "Função devolveu o valor errado, devia dar 5"
print("Função passou nos testes")