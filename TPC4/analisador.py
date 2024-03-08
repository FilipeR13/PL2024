import sys

import ply.lex as lex

reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'like': 'LIKE',
    'inner': 'INNER',
    'outer': 'OUTER',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full': 'FULL',
    'on': 'ON',
    # ...
}

tokens = [
    "FIELD",
    "COMMAND",
    "DELIMITER",
    "FINAL_DELIMITER",
    "NUMBER",
    "MATH_OPERATOR",
] + list(reserved.values())

def t_COMMAND(t):
    r'\b[a-zA-Z]+\b'
    if t.value.lower() in reserved:
        t.type = reserved.get(t.value.lower(), "COMMAND")
    else:
        t.type = "FIELD"
    return t

t_DELIMITER = r',' 

t_FINAL_DELIMITER = r';'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_MATH_OPERATOR(t):
    r">=|<=|\+|-|\*|>|<|="
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t'

def t_error(t):
    sys.stderr.write(f"Error: Unexpected character {t.value[0]}\n")
    t.lexer.skip(1) # Skip the character

def main(stdin):
    lexer = lex.lex()
    for linha in stdin:
        lexer.input(linha)
        for token in lexer:
            if not token: break 
            print(token)


if __name__ == '__main__':
    main(sys.stdin)