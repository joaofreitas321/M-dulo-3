# calcular a idade em anos
import datetime

dia = int(input("Dia de nascimento"))
mes = int(input("Mês de nascimento"))
ano = int(input("Ano de nascimento"))

#data atualk
hoje = datetime.date.today()

#objeto com a data de nascimento
data_nascimento = datetime.date(ano,mes,dia)

#calcular a idade
idade = hoje.year - data_nascimento.year
#verificar se ainda não fez anos este ano
if data_nascimento.month > hoje.month or (data_nascimento.month == hoje.month and data_nascimento.day > hoje.day):
    idade -= 1

print(idade)