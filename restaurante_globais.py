"""
O Sr Joaquim precisa de um programa para controlar o número de clientes e de mesas do
seu restaurante. O programa deve apresentar um menu com as opções: 1. Entrada,
2. Saída, 3. Estado, 4. Terminar
"""
import utils
    
def EntradaClientes():
    """
    Função responsável por registar a entrada dos clientes
    """
    global n_max_clientes
    global n_atual_clientes
    # testar se o restaurante não pode receber mais clientes
    if n_max_clientes == n_atual_clientes:
        print("Restaurante está cheio")
        return 0
    # ler o nº de clientes a entrar
    lugar_livres = n_max_clientes - n_atual_clientes
    entrar = utils.ler_numero_inteiro_limites(1,lugar_livres,"Quantos clientes:")
    # devolve o nº de clientes que entraram
    n_atual_clientes += entrar
def EntradaMesas():
    """
    Função responsável por registar a ocupação das mesas
    """
    global n_max_mesas
    global n_atual_mesas
    # testar se não tem mesas livres
    if n_max_mesas == n_atual_mesas:
        print("Restaurante está cheio")
        return 0
    mesas_livres = n_max_mesas - n_atual_mesas
    entrar = utils.ler_numero_inteiro_limites(1,mesas_livres,"Quantas mesas:")
    n_atual_mesas += entrar
    
def SaidaClientes():
    """
    Função responsável por registar a saída dos clientes
    """
    global n_atual_clientes
    global total_pago
    if n_atual_clientes == 0:
        print("Não tem clientes")
        return 0
    n_clientes = utils.ler_numero_inteiro_limites(1,n_atual_clientes, "Quantos clientes saiem do restaurante:")
    n_atual_clientes -= n_clientes
    pagou = utils.ler_numero_decimal_limites(0,None,'Quanto custou a refeição:')
    total_pago = total_pago + pagou
def SaidaMesas():
    """
    Função responsável por registar as mesas desocupadas
    """
    global n_atual_mesas
    if n_atual_mesas == 0:
        print("Não tem mesas ocupadas.")
        return 0
    n_mesas = utils.ler_numero_inteiro_limites(1,n_atual_mesas,"Quantas mesas ficaram desocupadas:")
    n_atual_mesas -= n_mesas
def Estado():
    """
    Função que calcula e mostra os dados estatísticos do estado do restaurante
    """
    print(f"Tem {n_atual_mesas} mesas ocupadas e {n_max_mesas - n_atual_mesas} mesas livres")
    print(f"Tem {n_atual_clientes} clientes no restaurante")
    print(f"Que corresponde a uma ocupação de {n_atual_clientes/n_max_clientes*100}%")
    print(f"Já recebeu {total_pago}€ das refeições servidas")

def Menu():
    op = 1
    while op != 4:
        op = utils.ler_numero_inteiro_limites(1,4,"1.Entrada\2.Saída\3.Estado\4.Terminar")
        if op == 1:
            # Entrada dos clientes
              EntradaClientes()
              EntradaMesas()   
        if op == 2:
            # Saída dos clientes
                SaidaClientes()
                SaidaMesas()
        if op == 3:
            Estado()

n_max_mesas = utils.ler_numero_inteiro("Quantas mesas tem o restaurante:")
n_max_clientes = utils.ler_numero_inteiro("Quantos clientes o restaurante pode ter:")
n_atual_mesas = 0
n_atual_clientes = 0
total_pago = 0


def Main():
    Menu()
if __name__=='__main__':
    Main()