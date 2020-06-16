# ssscobrazzz

sssRepositório da linguagem maisss sssensacional que 
qualquer cobra já viuzzz


## Como usar

python3 main.py ARQUIVO

### Inssspiração

Qualquer semelhança com python definitivamente não é coincidência. A linguagem das cobras herda boa parte da sintaxe do primo, mas deixa de lado a necessidade de uma identação perfeita, usando o sssom preferido das cobrazzz como marcação de bloco. 

### Exemplos

test_basic: prints, atribuição, funções (definição e chamada), aritmética

``` 

print(1)

def worker(arg1,arg2)
sss
    print(arg1*arg2)
    print(0)
    print(arg1+arg2)
    
    return arg1/arg2
zzz

a = 10
b = 4
print(a**(b-1))
print(worker(a,b))

```



test_med: Loop While, operações relacionais

```

loga = 3
logb = loga + 4

print(loga > logb)

while !(logb == loga) 
sss
    loga = loga + 1
zzz

print(loga)
print(logb)

```


test_adv: recursao

```

def fib(num)sss
    if num < 2 sss
        return num
    zzz else sss
        return fib(num-1) + fib(num-2)
    zzz
zzz

a = 10
bad = 0
while bad < a sss
    print(fib(bad))
    bad = bad+1
zzz 

``` 

## Definição da EBNF


```EBNF

program: block+
block: stmt+

funccall: NAME '(' [callargs] ')'
callargs: test (',' test)*

funcdef: 'def' NAME '(' [defargs] ')' 'sss' block 'zzz'
return_stmt: 'return' [test]
defargs: NAME (',' NAME)*


stmt: (test | return_stmt | while_stmt | if_stmt | assignment | print )

while_stmt: 'while' test 'sss' block 'zzz'

if_stmt: 'if' test 'sss' block 'zzz' ['else' 'sss' block 'zzz'] 


assignment: NAME '=' test

print: 'print' '(' test ')' 

test: or_test
or_test: and_test ('||' and_test)*
and_test: not_test ('&&' not_test)*
not_test: ('!' not_test | comp)

comp: expr ('<'|'>'|'==' expr)*
expr: term (('+'|'-') term)*
term: factor (('*'|'/') factor)*
factor: ('+'|'-') factor | power
power: atom ['**' factor] | '(' test ')'
atom: (NAME | NUMBER | funccall)



NAME : letra (letra|digito)*

NUMBER : digito+

``` 
