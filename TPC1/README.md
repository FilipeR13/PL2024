# TPC1: Estatísticas de exames médicos desportivos
## 2024/02/05

## Autor:
- A100692
- José Filipe Ribeiro Rodrigues

## Resumo

Neste trabalho, foi desenvolvido um ficheiro python (script.py) que lê um ficheiro .csv e calcula algumas estatísticas pedidas pelo docente.

Primeiramente, após ter lido todas as linhas do csv e ter guardado as mesmas numa lista de dicionários, cujos representam as colunas do dataset para ser de mais fácil acesso, a lista é ordenada consoante a modalidade, a qual é escrita no terminal para mostrar que a mesma está correta.

De seguida, a lista é filtrada pelos atletas aptos, obetendo assim o número total dos mesmos. Com este número calculado, apresentar a sua percentagem referente ao total de atletas é trivial.

Por fim, os atletas são organizados em faixas etárias. Para facilitar o cálculo da faixa, é aplicado uma simples fórmula, presente na função "find_interval()", apenas aplicando uma divisão inteira da idade com o tamanho do intervalo, 5, e multiplicando esse resultado ao mesmo tamanho do intervalo para assim obter o ínicio correspondente da faixa.
 