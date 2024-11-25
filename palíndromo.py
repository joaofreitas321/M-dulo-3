# Uma função que verifique se uma string é um palíndromo
def Palindromo(palavra) -> bool:
    palavra = palavra.lower()
    palavra_invertida = ""
    for posicao in range(len(palavra)-1,-1,-1):
        palavra_invertida = palavra_invertida + palavra[posicao]
    if palavra == palavra_invertida:
        return True
    return False

if Palindromo("Ana") == True:
    print("Ana é um palindromo")
else:
    print("Ana não é um palindromo")        