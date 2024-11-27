"""
Programa que com uma função com o nome soma_quadrados que recebe um nº inteiro positivo,
 n, e devolve a soma dos quadrados de todos os números inteiros positivos até n
 """
import quadrado

def soma_quadrados(n1):
    soma = 0
    for i in range(1,n1+1):
        q = quadrado.Quadrado(i)
        soma = soma + q
    return soma

assert soma_quadrados(3) == 14, "Valor devolvido devia ser 14"
assert soma_quadrados(5) == 55, "Valor devolvido devia ser 55"
print("A função passou nos testes")    