# Uma função que devolve o maior de dois nº. Se forem iguais devolve none
def maiordedois(n1,n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return None
    
assert maiordedois(10,5) == 10, "A função devia devolver 10"
assert maiordedois(10,10) == None, "A função devia devolver None porque os nº são iguais" 

print("A função passou todos os testes")