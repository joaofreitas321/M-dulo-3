"""
Implemente um programa que codifica ou descodifica uma mensagem com base nos alfabetos
fornecidos"""

original = "abcdefghijklmnopqrstuvwxyz"
codigo = "bcdefghijklmnopqrstuvwxyza"

def menu():
    """Função para ler a opção do utilizador e executar a função adequada: codificar ou
    descodificar"""
    print(codifica("ola mundo"))    

def codifica(mensagem:str)->str:
    """
    Função que recebe uma mensagem e devolve a mesma codificada de acordo com os alfabetos
    fornecidos"""
    global original
    global codigo
    texto = ""
    mensagem = mensagem.lower()
    for L in mensagem:
        #caso não encontre a letra no alfabeto deve manter a letra original
        if L not in original:
            texto = texto + L
        else:             
            for P in range(len(original)):
                if L == original[P]:
                    texto = texto + codigo[P]
    return texto            

def descodifica(mensagem_codificada:str)->str:
    """
    Função que recebe uma mensagem codificada e devolve a mesma descodificada de acordo com os
    alfabetos fornecidos"""
    global original
    global codigo
    texto = ""
    mensagem = mensagem.lower()
    for L in mensagem:
        #caso não encontre a letra no alfabeto deve manter a letra original
        if L not in codigo:
            texto = texto + L
        else:             
            for P in range(len(codigo)):
                if L == codigo[P]:
                    texto = texto + original[P]
    return texto            

def main():
    menu()

if __name__=='__main__':
    main()