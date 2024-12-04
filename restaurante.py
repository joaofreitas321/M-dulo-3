"""
O Sr Joaquim precisa de um programa para controlar o número de clientes e de mesas do
seu restaurante. O programa deve apresentar um menu com as opções: 1. Entrada,
2. Saída, 3. Estado, 4. Terminar
"""
import utils
    
def EntradaClientes(max_clientes,n_atual):
    """
    Função responsável por registar a entrada dos clientes
    """
    # testar se o restaurante não pode receber mais clientes
    if max_clientes == n_atual:
        print("Restaurante está cheio")
        return 0
    # ler o nº de clientes a entrar
    lugar_livres = max_clientes - n_atual
    entrar = utils.ler_numero_inteiro_limites(1,lugar_livres,"Quantos clientes:")
    # devolve o nº de clientes que entraram
    return entrar
def EntradaMesas(max_mesas,n_atual):
    """
    Função responsável por registar a ocupação das mesas
    """
    # testar se não tem mesas livres
    if max_mesas == n_atual:
        print("Restaurante está cheio")
        return 0
    mesas_livres = max_mesas - n_atual
    entrar = utils.ler_numero_inteiro_limites(1,mesas_livres,"Quantas mesas:")
    return entrar
def SaidaClientes(n_atual_clientes):
    """
    Função responsável por registar a saída dos clientes
    """
    if n_atual_clientes == 0:
        print("Não tem clientes")
        return 0
    n_clientes = utils.ler_numero_inteiro_limites(1,n_atual_clientes, "Quantos clientes saiem do restaurante:")
    return n_clientes
def SaidaMesas(n_atual_mesas):
    """
    Função responsável por registar as mesas desocupadas
    """
    if n_atual_mesas == 0:
        print("Não tem mesas ocupadas.")
        return 0
    n_mesas = utils.ler_numero_inteiro_limites(1,n_atual_mesas,"Quantas mesas ficaram desocupadas:")
    return n_mesas
def Estado(max_mesas,max_clientes,mesas,clientes):
    """
    Função que calcula e mostra os dados estatísticos do estado do restaurante
    """
    print(clientes)
def Menu():
    n_max_mesas = utils.ler_numero_inteiro("Quantas mesas tem o restaurante:")
    n_max_clientes = utils.ler_numero_inteiro("Quantos clientes o restaurante pode ter:")
    op = 1
    n_atual_mesas = 0
    n_atual_clientes = 0
    while op != 4:
        op = utils.ler_numero_inteiro_limites(1,4,"1.Entrada\2.Saída\3.Estado\4.Terminar")
        if op == 1:
            n_clientes_entraram = EntradaClientes(n_max_clientes,n_atual_clientes)
            n_mesas_ocupadas = EntradaMesas(n_max_mesas,n_atual_mesas)
            n_atual_clientes += n_clientes_entraram
            n_atual_mesas += n_mesas_ocupadas
        if op == 2:
            n_clientes_sairam = SaidaClientes(n_atual_clientes)
            n_mesas_desocupadas = SaidaMesas(n_atual_mesas)
            n_atual_clientes = n_atual_clientes - n_clientes_sairam
            n_atual_mesas = n_atual_mesas - n_mesas_desocupadas
        if op == 3:
            Estado(n_max_mesas,n_max_clientes,n_atual_mesas,n_atual_clientes)


def Main():
    Menu()
if __name__=='__main__':
    Main()