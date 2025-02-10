def Numero_perfeito(n) -> bool:
    soma = 0
    for i in range(1,n):
        if n % i == 0:
            soma = soma + i
    if soma == n:
        return True
    return False

def main():
    numero = int(input("Nº:"))
    if Numero_perfeito(numero) == True:
        print("Número perfeito")
    else:
        print("Número não perfeito")

if __name__=="__main__":
    main()                   