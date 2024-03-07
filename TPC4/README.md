# TPC4: Analisador Léxico
## 2024/03/02

## Autor:
- A100692
- José Filipe Ribeiro Rodrigues

## Resumo

Para este trabalho foi desenvolvido um analisador léxico que atribui tokens a uma linha sql:

`select id,name,salario from empregados where salario >= 820`

Desta forma, foram criados os seguintes tokens, cada um com o seu devido regex:

* FIELD
* COMMAND
* DELIMITER
* FINAL_DELIMITER
* NUMBER
* MATH_OPERATOR

Para além deste, existe ainda um token para cada tipo de instrução SQL (As instruções listadas podem ser encontradas no dicionário `reserved`)

Recorreu-se à biblioteca [ply](https://www.dabeaz.com/ply/ply.html), que é uma ferramenta para a construção de analisadores léxicos e sintáticos.
 
### Executar

Para executar o programa basta executar um dos seguintes comandos no terminal: `python3  analisador.py`