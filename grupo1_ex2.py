"""
Crie uma função que mostra a média de 5 valores. A função deve ler os valores
do utilizador e, posteriormente, calcular e mostrar a média dos valores
"""
def Media():
    soma = 0
    for _ in range(5):
        n = int(input("Introduza um nº:"))
        soma = soma + n
    media = soma / 5
    print(media)    