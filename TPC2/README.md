# TPC2: Conversor de MD para HTML
## 2024/02/21

## Autor:
- A100692
- José Filipe Ribeiro Rodrigues

## Resumo

Neste trabalho, foi desenvolvido um ficheiro python (script.py) que lê um ficheiro MarkDown e passa o seu conteúdo para um ficheiro html.

Para cumprir o desafio passado, foram desenvolvidas várias expressões regulares para cada encontrar cada tipo de sintaxe em ficheiros .md que são substítuidas por tags html. As expressões regulares encontram os vários níveis de títulos, texto em negrito ou itálico e ainda input de imagens ou links. Para além disso, o código python ainda deteta o ínicio e o fim das listas.

No fim, o resultado obtido após substituir as expressões por tags html é escrito num ficheiro chamado "output.html".