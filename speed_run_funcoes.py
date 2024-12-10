# João Freitas Nº10
# Exercício de Funções em Python
# Complete cada função conforme indicado na docstring.

def imprimir_dobro(valor):
    """Recebe um número e imprime o seu dobro."""
    dobro = valor * 2
    print(dobro)

def calcular_media_tres_numeros(n1, n2, n3):
    """
    Calcule a média aritmética de três números.
    Retorne o valor da média.
    """
    media = (n1 + n2 + n3) / 3
    return media
	
def calcular_fatorial(numero):
    """Recebe um número inteiro positivo e retorna o seu fatorial.
	    Fatorial de 5 (5!) = 5 * 4 * 3 * 2 * 1
	"""
    if numero < 0:
        return "Erro: nº inválido"
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    return fatorial     
    
def converter_celsius_para_fahrenheit(celsius):
    """
    Converta a temperatura de Celsius para Fahrenheit.
    Fórmula: (°C × 9/5) + 32 = °F
    """
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

def calcular_area_circulo(raio):
    """
    Calcule a área de um círculo dado o raio.
    Use pi = 3.14159
    """
    pi = 3.14159
    area = pi * (raio ** 2)
    return area

def exibir_contagem_regressiva(inicio):
    """Recebe um número e imprime uma contagem regressiva até 0."""
    for i in range(inicio, -1, -1):
        print(i)

def inverter_string(texto):
    """
    Receba uma string e retorne ela invertida.
    Exemplo: "python" -> "nohtyp"
    """
    texto_invertido = ""

    for i in range(len(texto)-1,-1):
        texto_invertido = texto_invertido + texto[i]
    return texto_invertido    

def verificar_divisibilidade(a, b):
    """Recebe dois números e imprime se o primeiro é divisível pelo segundo."""
    if b == 0:
        print("Não é possível dividir por zero")
    elif a % b:
        print(f"{a} é divisível por {b}")
    else:
        print(f"{a} não é divisível por {b}")    

def calcular_perimetro_circulo(raio):
    """Recebe o raio de um círculo e retorna o seu perímetro."""
    pi = 3.14159
    perimetro = 2 * pi * raio
    return perimetro

def converter_segundos_para_minutos(segundos):
    """Recebe um valor em segundos e retorna o correspondente em minutos."""
    minutos = segundos // 60
    segundos_restam = segundos % 60
    return F"{minutos}:{segundos_restam}"

def gerar_saudacao_periodo(hora_atual):
    """
    Retorne uma saudação baseada no período do dia.
    Se for antes de 12h: "Bom dia!"
    Entre 12h e 18h: "Boa tarde!"
    Após 18h: "Boa noite!"
    """
    if hora_atual < 12:
        return "Bom dia!"
    elif hora_atual >= 12 and hora_atual < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
	

def calcular_desconto(preco, percentual):
    """Recebe um preço e um percentual de desconto e retorna o preço com desconto."""
    desconto = preco * (percentual / 100)
    preco_com_desconto = preco - desconto
    return preco_com_desconto
    
def calcular_velocidade_media(distancia, tempo):
    """Recebe a distância percorrida e o tempo gasto e retorna a velocidade média."""
    if tempo == 0:
        return "Erro: o tempo não pode ser zero"
    return distancia / tempo

def verificar_palindromo(palavra):
    """
    Verifique se a palavra recebida é um palíndromo.
    Palíndromo é uma palavra que pode ser lida igual de trás para frente.
    Exemplo: "radar" é um palíndromo.
    """
    palavra = palavra.lower()
    palavra_invertida = ""
    for posicao in range(len(palavra)-1,-1,-1):
        palavra_invertida += palavra[posicao]
    if palavra == palavra_invertida:
        return True
    return False