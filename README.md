# ssscobrazzz
sssRepositório da linguagem maisss sssensacional que qualquer cobra já viuzzz


```EBNF

assignment = NAME "=" string | digito | NAME | expr ";"

comparison: expr (comp_op expr)*
comp_op: '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not'
expr: term (('+'|'-') term)*
term: factor (('*'|'/'|'%'|'//') factor)*
factor: ('+'|'-') factor | power
power: atom ['**' factor]
atom: (NAME | NUMBER | 'True' | 'False')



if_stmt: 'if' test 'sss' suite 'zzz' ('elif' test 'sss' suite 'zzz')* ['else' 'sss' suite 'zzz'] 
test: or_test
or_test: and_test ('or' and_test)*
and_test: not_test ('and' not_test)*
not_test: 'not' not_test | comparison
comparison: expr (comp_op expr)*


#Funões e loops 
while_stmt: 'while' test ':' suite ['else' ':' suite]
funcdef: 'def' NAME parameters 'sss' stmt+ 'zzz'

parameters: '(' [argslist] ')'
stmt: (expr | pass_stmt | return_stmt )

return_stmt: 'return' argslist ';'
pass_stmt: 'pass'

suite: stmt | sss stmt+ zzz

argslist: NAME {',' NAME}

NAME = letra {letra|digito}


``` 
