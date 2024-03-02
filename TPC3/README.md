# TPC3g: Contador On/Off
## 2024/02/26

## Autor:
- A100692
- José Filipe Ribeiro Rodrigues

## Resumo

Neste trabalho, foi desenvolvido um ficheiro python (countOnOff.py) que lê um ficheiro de texto e soma todos os digitos que estão entre ocorrências das palavras 'On' e 'Off'. Para além disso, se aparecer o caracter '=' deve ser impresso no terminal o resultado da soma atual.

Desta forma, de maneira a encontrar as várias ocorrências dos caracteres chaves foi desenvolvido um regex que deteta estas exatas sequências: `on|off|-?\d+|=`

Esta expressão regular é aplicada a todo o ficheiro, junto com a flag *re.IGNORECASE*, para detetar todas a variantes das palavras.

Após encontrar todas as ocorrências necessárias, foi apenas percorrido estas por ordem de aparição para assim conseguir calcular os valores supostos.

### Executar

Para executar o programa basta executar um dos seguintes comandos no terminal:
* python3 countOnOff.py < ex.txt
* cat ex.txt | python3 countOnOff.py

Assumindo q o ficheiro ex.txt existe