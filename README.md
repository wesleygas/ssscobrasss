# ssscobrazzz
sssRepositório da linguagem maisss sssensacional que qualquer cobra já viuzzz


```EBNF


program: block*
block: stmt*

assignment = NAME "=" comp

comp: expr ('<'|'>'|'==' expr)*
expr: term (('+'|'-') term)*
term: factor (('*'|'/') factor)*
factor: ('+'|'-') factor | power
power: atom ['**' factor]
atom: (NAME | NUMBER)



if_stmt: 'if' test 'sss' suite 'zzz' ('elif' test 'sss' suite 'zzz')* ['else' 'sss' suite 'zzz'] 
test: or_test
or_test: and_test ('or' and_test)*
and_test: not_test ('and' not_test)*
not_test: '!' not_test | comp


#Funões e loops 
while_stmt: 'while' test 'sss' suite 'zzz' ['else' 'sss' suite 'zzz']
funcdef: 'def' NAME parameters 'sss' stmt+ 'zzz'

parameters: '(' [argslist] ')'

print: '(' comp ')' 

stmt: (comp | return_stmt | while_stmt | if_stmt | assignment | print)

return_stmt: 'return' comp

suite:  stmt+

argslist: NAME (',' NAME)*

NAME = letra (letra|digito)*

NUMBER = digito+

``` 
