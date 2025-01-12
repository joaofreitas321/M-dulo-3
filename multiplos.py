"""
Um programa com uma função que, sendo dado como parâmetro de entrada de 
um nº inteiro, calcule e aprsente no monitor, todos os seus multiplos
inferiores a 100.
"""
def Multiplos_inferiores_a_100(n):
    if n <= 0:
        print("O número tem de ser maior que zero")
        return
    for i in range(n,100,n):
        print(i)

Multiplos_inferiores_a_100(8)        