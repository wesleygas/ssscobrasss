# ssscobrazzz
sssRepositório da linguagem maisss sssensacional que qualquer cobra já viuzzz


```EBNF

program: stmt*

assignment = NAME "=" digito | NAME | expr

comparison: expr (comp_op expr)*
comp_op: '<'|'>'|'=='
expr: term (('+'|'-') term)*
term: factor (('*'|'/') factor)*
factor: ('+'|'-') factor | power
power: atom ['**' factor]
atom: (NAME | NUMBER)



if_stmt: 'if' test 'sss' suite 'zzz' ('elif' test 'sss' suite 'zzz')* ['else' 'sss' suite 'zzz'] 
test: or_test
or_test: and_test ('or' and_test)*
and_test: not_test ('and' not_test)*
not_test: '!' not_test | comparison


#Funões e loops 
while_stmt: 'while' test 'sss' suite 'zzz' ['else' 'sss' suite 'zzz']
funcdef: 'def' NAME parameters 'sss' stmt+ 'zzz'

parameters: '(' [argslist] ')'
stmt: (expr | return_stmt | while_stmt | if_stmt | assignment)

return_stmt: 'return' NUMBER | argslist

suite:  stmt+

argslist: NAME (',' NAME)*

NAME = letra (letra|digito)*

NUMBER = digito+

``` 
