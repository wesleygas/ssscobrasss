# ssscobrazzz
sssRepositório da linguagem maisss sssensacional que qualquer cobra já viuzzz


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


assignment : NAME "=" test

print: 'print' '(' test ')' 

test: or_test
or_test: and_test ('||' and_test)*
and_test: not_test ('&&' not_test)*
not_test: ('!' not_test | comp)

comp: expr ('<'|'>'|'==' expr)*
expr: term (('+'|'-') term)*
term: factor (('*'|'/') factor)*
factor: ('+'|'-') factor | power
power: atom ['**' factor]
atom: (NAME | NUMBER | funccall)



NAME : letra (letra|digito)*

NUMBER : digito+

``` 
