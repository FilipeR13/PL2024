# Gramática Independente de Contexto
## 2024/03/02

## Autor:
- A100692
- José Filipe Ribeiro Rodrigues

## Resumo


Este trabalho consiste na implementação de uma gramática livre de contexto para representar expressões aritméticas e lógicas simples. A partir de um conjunto de exemplos dados, que podemos observar de seguida, foi desenvolvido a gramática que comprova estas mesmas expressões.
### Exemplos de Expressões

```
$ ?a
$ b=a*2/(27-3)
$ !a+b
$ c=(a*b)/(a/b)
```

## Resolução

```
T = {'!', '?', '(', ')', '=', '+', '-', '*', '/', var, num}

N = {S, Expr, Expr2, Expr3, Op, Op2}

S = S

P = {
    
    S -> '?' var            LA = {'?'}
       | '!' Expr           LA = {'!'}  
       | var '=' Expr       LA = {var} 

    Expr -> Expr2 Op

    Op -> '+' Expr          LA = {'+'}
        | '-' Expr          LA = {'-'}               
        | &                 LA = {$, ')'}
    
    Expr2 -> Expr3 Op2      LA = {'(', var, num}

    Op2 -> '*' Expr         LA = {'*'}
         | '/' Expr         LA = {'/'}
         | &                LA = {'+', '-', $, ')'}
    
    Expr3 -> '(' Expr ')'   LA = {'('}
           | var            LA = {var}
           | num            LA = {num}

}
```