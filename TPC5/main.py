import sys
import json
import ply.lex as lex

tokens = [
    'LISTAR',
    'MOEDA',
    'SAIR',
    'SELECIONAR',
    'ADICIONAR',
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

def t_ADICIONAR(t):
    r'adicionar[ ][\w-]+[ ]\d([ ]\d+(\.\d+)?)?'
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
    print("Bem-vindo à máquina de venda automática")
    for line in sys.stdin:
        lexer.input(line)
        for token in lexer:
            if not token: break 
            if token.type == "LISTAR":
                print('     Número     |            Nome                              |       Preço     |      Quantidade')
                for produto in produtos:
                    print(f'       {produto["id"]}        |        {produto["nome"]: <30}        |       {produto["preco"]}       |       {produto["quantidade"]}')
            elif token.type == "MOEDA":
                moedas = token.value.split(" ")[1].split(",")
                for moeda in moedas:
                    if moeda[-1] == "e":
                        saldo += float(moeda[:-1])
                    else:
                        saldo += round(float(moeda[:-1]) / 100,2)
                print(f"maq: Saldo: {saldo}€")
            
            elif token.type == "SAIR":
                print(f"maq: Troco: {round(saldo,2)}")
                change = get_change(saldo)
                for coin in change:
                    if change[coin] > 0:
                        print(f"{coin}€: {change[coin]}")
                return
            elif token.type == "SELECIONAR":
                id = int(token.value.split(" ")[1])
                if id in tabela:
                    if tabela[id]["quantidade"] > 0:    
                        produto = tabela[id]
                        if saldo >= produto["preco"]:
                            saldo -= produto["preco"]
                            tabela[id]["quantidade"] -= 1
                            print(f"maq: Produto {produto['nome']} comprado com sucesso")
                        else:
                            print(f"maq: Saldo insuficiente\nmaq: Saldo={saldo}€; Preço={produto['preco']}€")
                    else :
                        print(f"maq: Produto com id {id} esgotado")
                else:
                    print(f"maq: Produto com id {id} não existe")
            elif token.type == "ADICIONAR":
                nome = token.value.split(" ")[1]
                quantidade = int(token.value.split(" ")[2])
                for produto in produtos:
                    if produto["nome"] == nome:
                        produto["quantidade"] += quantidade
                        break
                else:
                    if len(token.value.split(" ")) == 4:
                        preco = float(token.value.split(" ")[3])
                        produtos.append({"id": len(produtos)+1, "nome": nome, "preco": preco, "quantidade": quantidade})
                    else:
                        print(f"maq: Produto {nome} não existe e não foi dado um preço para o novo produto")
                print(f"maq: Adicionada quantidade {quantidade} ao produto {nome}")

if __name__ == "__main__":
    main(sys.argv)