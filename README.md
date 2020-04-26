# ssscobrazzz
sssRepositório da linguagem maisss sssensacional que qualquer cobra já viuzzz


```EBNF


block: stmt*


#Funões e loops 
funcdef: 'def' NAME parameters 'sss' stmt+ 'zzz'
return_stmt: 'return' [test]
parameters: '(' [argslist] ')'

while_stmt: 'while' test 'sss' block 'zzz'

if_stmt: 'if' test 'sss' block 'zzz' ['else' 'sss' block 'zzz'] 

stmt: (test | return_stmt | while_stmt | if_stmt | assignment | print)

assignment = NAME "=" test

print: '(' test ')' 

test: or_test
or_test: and_test ('||' and_test)*
and_test: not_test ('&&' not_test)*
not_test: ('!' not_test | comp)

comp: expr ('<'|'>'|'==' expr)*
expr: term (('+'|'-') term)*
term: factor (('*'|'/') factor)*
factor: ('+'|'-') factor | power
power: atom ['**' factor]
atom: (NAME | NUMBER)

argslist: NAME (',' NAME)*

NAME = letra (letra|digito)*

NUMBER = digito+

``` 
