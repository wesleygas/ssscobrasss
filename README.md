# ssscobrazzz
sssRepositório da linguagem maisss sssensacional que qualquer cobra já viuzzz


```EBNF


block: stmt*


if_stmt: 'if' test 'sss' block 'zzz' ('elif' test 'sss' block 'zzz')* ['else' 'sss' block 'zzz'] 



#Funões e loops 
while_stmt: 'while' test 'sss' block 'zzz' ['else' 'sss' block 'zzz']
funcdef: 'def' NAME parameters 'sss' stmt+ 'zzz'

parameters: '(' [argslist] ')'

print: '(' test ')' 

stmt: (test | return_stmt | while_stmt | if_stmt | assignment | print)

return_stmt: 'return' test

assignment = NAME "=" test

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
