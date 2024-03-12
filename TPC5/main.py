import sys
import json
import ply.lex as lex

tokens = [
    'LISTAR',
    'MOEDA',
    'SAIR',
    'SELECIONAR'   
]

def t_LISTAR(t):
    r'listar'
    return t

def t_MOEDA(t):
    r'moeda[ ]([2e|1e|5c|10c|20c|50c],?)+'
    return t

def t_SAIR(t):
    r'sair'
    return t

def t_SELECIONAR(t):
    r'selecionar[ ]\d+'
    return t

t_ignore = '\t\n'

def t_error(t):
    sys.stderr.write(f"Error: Unexpected command {t.value[0]}\n")
    t.lexer.skip(1) # Skip the character

def get_change(saldo):
    change = {}
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05]
    for coin in coins:
        change[coin] = int(saldo // coin)
        saldo = round(saldo % coin, 2)
    return change


def main(argv):
    if (len(argv) < 2):
        print("Usage: python main.py <input_file>")
        return

    input_file = argv[1]
    with open(input_file, "r") as file:
        data = json.load(file)
    
    produtos = data["produtos"]
    tabela = {}
    for produto in produtos:
        tabela[produto["id"]] = produto

    lexer = lex.lex()

    saldo = 0

    for line in sys.stdin:
        lexer.input(line)
        for token in lexer:
            if not token: break 
            if token.type == "LISTAR":
                print('     Número     |            Nome                              |       Preço')
                for produto in produtos:
                    print(f'       {produto["id"]}        |        {produto["nome"]: <30}        |       {produto["preco"]}')
            elif token.type == "MOEDA":
                moedas = token.value.split(" ")[1].split(",")
                for moeda in moedas:
                    if moeda[-1] == "e":
                        saldo += float(moeda[:-1])
                    else:
                        saldo += float(moeda[:-1]) / 100
                print(f"Saldo: {saldo}€")
            
            elif token.type == "SAIR":
                print(f"Troco: {round(saldo,2)}")
                change = get_change(saldo)
                for coin in change:
                    if change[coin] > 0:
                        print(f"{coin}€: {change[coin]}")
                return
            elif token.type == "SELECIONAR":
                id = int(token.value.split(" ")[1])
                if id in tabela:
                    produto = tabela[id]
                    if saldo >= produto["preco"]:
                        saldo -= produto["preco"]
                        print(f"Produto {produto['nome']} comprado com sucesso")
                    else:
                        print("Saldo insuficiente")
                else:
                    print(f"Produto com id {id} não existe")


if __name__ == "__main__":
    main(sys.argv)