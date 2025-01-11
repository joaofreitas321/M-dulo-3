"""
Um programa em que uma gangue quer dividir o dinheiro que roubaram de um banco. O líder quer
ficar com metade do dinheiro. Os dois elementos do gangue que correm mais riscos também 
querem ficar com metade. O outro que só conduz o carro não tem de correr riscos sérios
por isso ele receberia metade do dinheiro dos dois anteriores.
Calcula o valor a distribuir por cada elemento do grupo de acordo com o valor que o assalto
rendeu.
Para não levantar suspeitas cada membro quer gastar o dinehiro que resultou do assalto
de forma controlada, assim cada um quer gastar 5% do que recebeu por mês, desde que não
ultrapasse os 1000€. Calcula para cada um quanto tempo (meses) o dinheiro vai "durar".
Como os assaltantes são cuidadosos com o dinheiro querem guardar algum para a reforma,
assim pretende depositar 50% do dinheiro no banco que assaltaram que oferece uma taxa
de juro de 5% por ano. Calcula quanto dinheiro eles vão ter ao fim de 10 anos.
"""
import math
def ValorAssalto():
    dinheiro = 0
    while dinheiro <= 0:
        dinheiro = float(input("Introduza quanto rendeu o assalto:"))
    return dinheiro

def CalcularMeses(valor):
    """Calcular o valor a gastar por mês e mostrar em quantos meses se gasta o dinheiro"""
    #calcular 5% do valor
    valor_mes = valor * 0.05
    #calcular se ultrapassa os 1000€
    if valor_mes > 1000:
        valor_mes = 1000 
    #calcular quantos meses demora a gastar o dinheiro todo
    meses = valor / valor_mes
    meses = math.ceil(meses)
    print(f"Os {valor}€ são gastos em {meses} meses, gastando {valor_mes}€ por mês.")

def main():
    #pedir o valor que rendeu o assalto
    valor_assalto = ValorAssalto()
    #calcular a parte do lider 50%
    valor_lider = round(valor_assalto * 0.5,2)
    print(f"O líder recebe {valor_lider}")
    #calcular o valor dos dois elementos 20%
    valor_dois = round(valor_assalto * 0.2,2)
    print(f"Os dois elementos seguintes recebem {valor_dois}")
    #calcular o valor do condutor 10%
    valor_condutor = round(valor_assalto * 0.1,2)
    print(F"O condutor recebe {valor_condutor}")
    #calcular quanto pode gastar cada um
    CalcularMeses(valor_lider)
    CalcularMeses(valor_dois)
    CalcularMeses(valor_condutor)
    #calcular o valor do deposito a 10 anos

if __name__=="__main__":
    main() 