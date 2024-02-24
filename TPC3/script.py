import sys
import re

count = False
soma = 0
data = sys.stdin.read()

regex_on = re.compile(r'[oO][nN]')
regex_off = re.compile(r'[oO][fF]{2}')
regex_digit = re.compile(r'\d+')
regex_equals = re.compile(r'=')
regex_serach_valid_digits = re.compile(r'([oO][nN])(.*?)([oO][fF]{2})')

for linha in data.split("\n"):
    match_on = list(regex_on.finditer(linha))
    match_off = list(regex_off.finditer(linha))
    match_digit = list(regex_digit.finditer(linha))
    match_equals = list(regex_equals.finditer(linha))

    if match_digit:
        # if theres an on in the line and not a off it means that all numbers after the on are to be summed
        if match_on and not match_off:
            # print("Entrei aqui 1")
            if count:
                for x in match_digit:
                    while match_equals and x.start() > match_equals[0].start():
                        print("Current Sum:" + str(soma))
                        match_equals = match_equals[1:]
                    soma += int(x.group())
            else:
                for x in match_digit:
                    while match_equals and x.start() > match_equals[0].start():
                        print("Current Sum:" + str(soma))
                        match_equals = match_equals[1:]
                    if x.start() > match_on[0].start():
                        soma += int(x.group())
            while match_equals:
                print("Current Sum:" + str(soma))
                match_equals = match_equals[1:]
            count = True

        # if theres an off in the line and not a on it means that all numbers before the off are to be summed
        elif match_off and not match_on:
            # print("Entrei aqui 2")
            for x in match_digit:
                while match_equals and x.start() > match_equals[0].start():
                    print("Current Sum:" + str(soma))
                    match_equals = match_equals[1:]
                if x.start() < match_off[0].start():
                    soma += int(x.group())
                else:
                    break
            while match_equals:
                print("Current Sum:" + str(soma))
                match_equals = match_equals[1:]

        # if theres any on or off and if count is True it means that all numbers are to be summed
        elif not match_on and not match_off:
            # print("Entrei aqui 3")
            if count:
                for x in match_digit:
                    while match_equals and x.start() > match_equals[0].start():
                        print("Current Sum:" + str(soma))
                        match_equals = match_equals[1:]
                    soma += int(x.group())
                for x in match_equals:
                    print("Current Sum:" + str(soma))
                    match_equals = match_equals[1:]
            elif match_equals:
                print ("Current Sum:" + str(soma) for _ in match_equals)

        # if theres an off and an on in the line it means that all numbers between the on and the off are to be summed
        elif match_off and match_on:
            on_in_last = False if match_off[-1].start() > match_on[-1].start() else True
            digits_valids = list(regex_serach_valid_digits.finditer(linha))
            # print ("Digits Valids: ", digits_valids)

            if count:
                while match_digit and digits_valids and digits_valids[0].start() > match_digit[0].start():
                    while match_equals and match_digit[0].start() > match_equals[0].start():
                        print("Current Sum:" + str(soma))
                        match_equals = match_equals[1:]
                    soma += int(match_digit[0].group())
                    match_digit = match_digit[1:]
            
            while match_equals and digits_valids and digits_valids[0].start() > match_equals[0].start():
                print("Current Sum:" + str(soma))
                match_equals = match_equals[1:]

            for x in digits_valids:
                while match_equals and x.start() > match_equals[0].start():
                    print("Current Sum:" + str(soma))
                    match_equals = match_equals[1:]
                digits = list(regex_digit.finditer(x.group(2)))
                equals_within = list(regex_equals.finditer(x.group(2)))

                for y in digits:
                    while equals_within and y.start() > equals_within[0].start():
                        print("Current Sum:" + str(soma))
                        equals_within = equals_within[1:]
                        match_equals = match_equals[1:]
                    soma += int(y.group())

                while equals_within:
                    print("Current Sum:" + str(soma))
                    equals_within = equals_within[1:]
                    match_equals = match_equals[1:]
            if on_in_last:
                remaing_digits = list(regex_digit.finditer(linha[digits_valids[-1].end():]))
                remaing_equals = list(regex_equals.finditer(linha[digits_valids[-1].end():]))
                for x in remaing_digits:
                    while remaing_equals and x.start() > remaing_equals[0].start():
                        print("Current Sum:" + str(soma))
                        remaing_equals = remaing_equals[1:]
                        match_equals = match_equals[1:]
                    soma += int(x.group())

                while remaing_equals:
                    print("Current Sum end:" + str(soma))
                    remaing_equals = remaing_equals[1:]
                    match_equals = match_equals[1:]
            count = on_in_last

    elif match_equals:
        print ("Current Sum:" + str(soma) for _ in match_equals)
    # print("line " + linha,match_digit, match_on, match_off, match_equals,soma, count, '\n')