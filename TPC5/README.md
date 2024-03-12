# Simulador de Máquina de Vendas
## 2024/03/02

## Autor:
- A100692
- José Filipe Ribeiro Rodrigues

## Resumo

Este programa, desenvolvido em Python, simula o comportamento de uma máquina de vendas. Ele permite que os utilizadores interajam com a máquina inserindo comandos para listar produtos, adicionar moedas, selecionar produtos para compra e sair do mesmo.

## Resolução

Tal como foi referido anteriormente, o programa foi desenvolvido em Python, aproveitando a biblioteca `ply.lex` para realizar análise léxica e interpretar os comandos fornecidos pelo utilizador.

### Análise Léxica com PLY

Foram criados vários tokens para cada operação possível na máquina de vendas:

1. `LISTAR`
2. `MOEDA`
3. `SELECIONAR`
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
- **MOEDA:** Adicionar moedas à máquina.
- **SELECIONAR:** Selecionar um produto para compra.
- **SAIR:** Sair da simulação e receber troco.

## Exemplo de Uso

```
$ listar
     Número     |            Nome                              |       Preço
       1        |        Agua                                  |       0.6
       2        |        Coca-Cola                             |       0.9
       3        |        Palmier                               |       0.7
       3        |        Croassant Misto                       |       1.2
$ moeda 1e
Saldo: 1.0€
$ selecionar 2
Produto Coca-Cola comprado com sucesso
$ sair
Troco: 0.1
0.1€: 1
```
