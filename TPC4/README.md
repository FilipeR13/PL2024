# TPC2: Analisador Léxico
## 2024/03/02

## Autor:
- A100692
- José Filipe Ribeiro Rodrigues

## Resumo

Para este trabalho foi desenvolvido um analisador léxico que atribui tokens a uma linha sql:

`select id,name,salario from empregados where salario >= 820`

Desta forma, foram criados os seguintes tokens, cada um com o seu devido regex:

* SELECT
* FROM
* WHERE
* ID
* COMMA
* GREATER
* NUM
* SKIP
* ERRO

Desta forma é impresso no terminal todos os matches por ordem.
 
### Executar

Para executar o programa basta executar um dos seguintes comandos no terminal: `python3  analisador.py`