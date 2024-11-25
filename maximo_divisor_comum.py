# Uma função que encontre o máximo divisor comum (MDC) entre dois numeros
def Maiordivisor(n1,n2):
    menor = n1
    if n2 < menor:
        menor = n2
    maior_divisor = None    
    for i in range(2,menor):
        if n1 % i == 0 and n2 % i == 0:
            maior_divisor = i
    return maior_divisor

assert Maiordivisor(6,12) == 3, "O maior divisor de 6 e 12 é 3"
assert Maiordivisor(12,6) == 3, "O maior divisor de 12 e 6 é 3"
assert Maiordivisor(5,10) == None, "Não existe maior divisor entre 5 e 10"
print("A função passou todos os testes")