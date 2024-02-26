import re, sys


data = sys.stdin.read()

soma = 0
on = False

matchs = re.finditer(r'on|off|-?\d+|=', data, re.IGNORECASE)

for found in matchs:
    print (found.group())
    if found.group().lower() == 'on':
        on = True
    elif found.group().lower() == 'off':
        on = False
    elif found.group() == '=':
        print("Current Sum: " + str(soma))
    elif on:
        soma += int(found.group())