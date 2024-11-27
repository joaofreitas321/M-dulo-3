# Programa que quando uma pessoa entra no parque de estacionamento saber quantos minutos lá esteve
from datetime import datetime
def DuracaoEstacionamento(hora:int,minutos:int) ->int:
    """
    Função que calcula a duração do estacionamento em minutos com base nos valores dos parâmetros e a hora atual
    """
    hora_atual = datetime.now().hour
    minutos_atuais = datetime.now().minute
    n_horas = hora_atual - hora
    n_minutos = minutos_atuais - minutos
    if n_minutos < 0:
        n_horas -= 1
        n_minutos = 60 - minutos + minutos_atuais
    duracao_total_minutos = n_horas * 60 + n_minutos
    return duracao_total_minutos

def BlocosMinutos(minutos:int)-> int:
    """
    Função que recebe a duração em minutos e devolve quantos blocos de 15 minutos existem"""
    n_blocos = minutos // 15
    if minutos % 15 != 0:
        n_blocos += 1
    return n_blocos    

def Custo(blocos:int,preco_bloco:float)->float:
    """
    Função que calcula o custo do estacionamento com base na duração em blocos de 15 min e o preço de cada
    bloco
    """
    return blocos * preco_bloco

def main():
    # ler dados
    preco = float(input("Qual o preço por cada 15 minutos"))
    hora = int(input("Introduza a hora a que entrou"))
    minutos = int(input("Quais os minutos de entrada no parque"))
    #calcular a duração em minutos
    duracao_minutos = DuracaoEstacionamento(hora,minutos)
    blocos = BlocosMinutos(duracao_minutos)
    print(duracao_minutos)
    #calcular o custo
    custo = Custo(blocos,preco)
    #mostrar o resultado
    print(f"Estacionamento com duração de {duracao_minutos} minutos que corresponde a {blocos} blocos de 15 minutos com o custo de {custo}€")      

if __name__=='__main__':
    main()