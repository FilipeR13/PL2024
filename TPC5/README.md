# Simulador de Máquina de Vendas
## 2024/03/02

## Autor:
- A100692
- José Filipe Ribeiro Rodrigues

## Resumo

Este programa, desenvolvido em Python, simula o comportamento de uma máquina de vendas. Ele permite que os utilizadores interajam com a máquina inserindo comandos para listar produtos, adicionar moedas, selecionar produtos para compra, adicionar produtos ao stock e sair do mesmo.

## Resolução

Tal como foi referido anteriormente, o programa foi desenvolvido em Python, aproveitando a biblioteca `ply.lex` para realizar análise léxica e interpretar os comandos fornecidos pelo utilizador.

### Análise Léxica com PLY

Foram criados vários tokens para cada operação possível na máquina de vendas:

1. `LISTAR`
2. `MOEDA`
3. `SELECIONAR`
3. `ADICIONAR`
4. `SAIR`

Cada token tem associado uma expressão regular associada permitindo identificar e classificar corretamente as entradas do utilizador.

### Interação com o Utilizador

- **Entrada de Comandos:** O programa aguarda a entrada do utilizador por meio do terminal, onde ele pode inserir os comandos desejados para interagir com a máquina de vendas.
- **Processamento de Comandos:** Cada comando fornecido pelo utilizador é interpretado e executado pelo programa, permitindo listar produtos, adicionar moedas, selecionar produtos para compra e sair da simulação.
- **Feedback ao utilizador:** O programa fornece feedback ao utilizador em cada etapa da interação, informando sobre o status da operação realizada e fornecendo detalhes relevantes, como troco e disponibilidade de produtos.

### Manipulação de Dados do Produto

- **Formato de Dados:** A lista de produtos da máquin são extraídos de um ficheiro JSON, seguindo uma estrutura específica que inclui o ID do produto, o nome e o preço.
- **Carregamento de Dados:** O programa carrega os dados a partir do ficheiro do formato especificado em cima passado como argumento, escrevendo os dados necessários em memória numa estrutura selhante à escrita no ficheiro.

## Instruções de Uso


Execute o programa a partir do terminal ou prompt de comando, fornecendo o arquivo JSON como argumento.

```
python3 main.py lista.json
```

### Lista de Comandos

- **LISTAR:** Exibir todos os produtos na máquina de vendas.
  - Argumentos: Não possui
- **MOEDA:** Adicionar moedas à máquina.
  - Argumentos: Moedas (Lista de moedas separado por `,` (ex: "1e,20c"))
- **SELECIONAR:** Selecionar um produto para compra.
  - Argumentos: Id
- **ADICIONAR:** Adicionar produtos à máquina, existentes ou não existentes.
  - Argumentos: Nome Quantidade [preco](caso o produto seja novo)
- **SAIR:** Sair da simulação e receber troco.
  - Argumentos: Não possui

## Exemplo de Uso

```
Bem-vindo à máquina de venda automática
$ listar
     Número     |            Nome                              |       Preço     |      Quantidade
       1        |        Agua                                  |       0.6       |       10
       2        |        Coca-Cola                             |       0.9       |       1
       3        |        Palmier                               |       0.7       |       10
       3        |        Croassant Misto                       |       1.2       |       10
$ adicionar fanta 3 0.8
maq: Adicionada quantidade 3 ao produto fanta
$ listar
     Número     |            Nome                              |       Preço     |      Quantidade
       1        |        Agua                                  |       0.6       |       10
       2        |        Coca-Cola                             |       0.9       |       1
       3        |        Palmier                               |       0.7       |       10
       3        |        Croassant Misto                       |       1.2       |       10
       5        |        fanta                                 |       0.8       |       3
$ moeda 1e,50c
maq: Saldo: 1.5€
$ selecionar 2
maq: Produto Coca-Cola comprado com sucesso
$ selecionar 2
maq: Produto com id 2 esgotado
$ selecionar 3
maq: Saldo insuficiente
maq: Saldo=0.6€; Preço=1.2€
$ listar
     Número     |            Nome                              |       Preço     |      Quantidade
       1        |        Agua                                  |       0.6       |       10
       2        |        Coca-Cola                             |       0.9       |       0
       3        |        Palmier                               |       0.7       |       10
       3        |        Croassant Misto                       |       1.2       |       10
       5        |        fanta                                 |       0.8       |       3
$ sair
maq: Troco: 0.6
0.5€: 1
0.1€: 1
```
