"""
Programa que para cada letra do alfabeto português, indique o número de vezes que 
aparece na frase. Todos os carateres que não pertencerem ao alfabeto português não
devem ser contabilizados. 
"""
alfabeto = "abcdefghijklmnopqrstuvwxyz"

def ContarLetra(letra,frase):
    #Função para contar quantas vezes a letra aparece na frase
    contar = 0
    for l in frase:
        if letra == l:
            contar = contar + 1
    return contar

def ContarFrequencia(frase):
    #Função que mostra o nº de vezes que cada letra do alfabeto aparace na frase
    #percorrer o alfabeto
    for i in range(97,123): # 97 =>a 122 =>z
        contar = ContarLetra(chr(i),frase)
        print(f"{chr(i)} - {contar}")

frase = input("Introduza uma frase:")
ContarFrequencia(frase)