# Uma função que recebe um número e indica se é primo ou não
def Primo(n1) -> bool:
    E_Primo = True
    for i in range(2,n1):
        if n1 % i == 0:
            E_Primo = False
            break
    return E_Primo 

#if Primo(3) == True:
#   print("O nº 3 é primo")
#else:
#    print("O nº 3 não é primo")

#if Primo(8) == True:
#    print("O nº 8 é primo")
#else:
#    print("O nº 8 não é primo")          