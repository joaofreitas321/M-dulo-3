"""
Programa que lê as coordernadas de um ponto P(x,y) e vê se está no 1º, no 2º,
no 3º ou no 4º quadrante
"""
x = int(input("Introduza a coordenada x do ponto"))
y = int(input("Introduza a coordenada y do ponto"))

def Coordenadas():
    if x == 0 and y == 0:
        print("Estão no ponto 0,0")
    elif x >= 1 and y >= 1:
        print("Estão no 1º quadrante")
    elif x < 1 and y >= 1:
        print("Estão no 2º quadrante")
    elif x < 1 and y < 1:
        print("Estão no 3º quadrante")
    elif x >= 1 and y < 1:
        print("Estão no 4º quandrante")
    else:
        print("Não está em nenhum quadrante")

Coordenadas()