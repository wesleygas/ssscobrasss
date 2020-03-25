# ssscobrasss
sssRepositório da linguagem maisss sssensacional que qualquer cobra já viusss


```EBNF

VARIAVEL = NAME "=" string | digito | identificador | expr ";"

comparison: expr (comp_op expr)*
comp_op: '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not'
testlist_star_expr: (test|star_expr) (',' (test|star_expr))* [',']
star_expr: '*' expr
expr: xor_expr ('|' xor_expr)*
xor_expr: and_expr ('^' and_expr)*
and_expr: shift_expr ('&' shift_expr)*
shift_expr: arith_expr (('<<'|'>>') arith_expr)*
arith_expr: term (('+'|'-') term)*
term: factor (('*'|'@'|'/'|'%'|'//') factor)*
factor: ('+'|'-'|'~') factor | power
power: atom ['**' factor]
atom: (NAME | NUMBER | STRING+ | 'None' | 'True' | 'False')

STRING = """ identificador """

if_stmt: 'if' namedexpr_test 'sss' suite 'zzz' ('elif' namedexpr_test 'sss' suite 'zzz')* ['else' 'sss' suite 'zzz'] 
namedexpr_test: test [':=' test]
test: or_test ['if' 'sss' or_test 'zzz' 'else' 'sss' test 'zzz']
or_test: and_test ('or' and_test)*
and_test: not_test ('and' not_test)*
not_test: 'not' not_test | comparison
comparison: expr (comp_op expr)*

NAME = letra {letra|digito}


#Funões e loops 
for_stmt: 'for' exprlist 'in' testlist 'sss' [TYPE_COMMENT] suite 'zzz' ['else' 'sss' suite 'zzz']
funcdef: 'def' NAME parameters 'sss' stmt+ 'zzz'

parameters: '(' [typedargslist] ')'
stmt: (testlist_star_expr | pass_stmt | flow_stmt | import_stmt)
while_stmt: 'while' namedexpr_test ':' suite ['else' ':' suite]
return_stmt: 'return' [testlist_star_expr] ';'
flow_stmt: break_stmt | continue_stmt | return_stmt ';'
break_stmt: 'break'
del_stmt: 'del' exprlist
pass_stmt: 'pass'
continue_stmt: 'continue'

suite: simple_stmt | sss stmt+ zzz

#IMPORTS
import_stmt: import_name | import_from ';'
import_name: 'import' dotted_as_names
import_from: ('from' (('.')* dotted_name | ('.')+)
              'import' ('*' | '(' import_as_names ')' | import_as_names))
import_as_name: NAME ['as' NAME]
dotted_as_name: dotted_name ['as' NAME]
import_as_names: import_as_name (',' import_as_name)* [',']
dotted_as_names: dotted_as_name (',' dotted_as_name)*
dotted_name: NAME ('.' NAME)*


typedargslist: (
  (tfpdef ['=' test] (',' [TYPE_COMMENT] tfpdef ['=' test])* ',' [TYPE_COMMENT] '/' [',' [ [TYPE_COMMENT] tfpdef ['=' test] (
        ',' [TYPE_COMMENT] tfpdef ['=' test])* (TYPE_COMMENT | [',' [TYPE_COMMENT] [
        '*' [tfpdef] (',' [TYPE_COMMENT] tfpdef ['=' test])* (TYPE_COMMENT | [',' [TYPE_COMMENT] ['**' tfpdef [','] [TYPE_COMMENT]]])
      | '**' tfpdef [','] [TYPE_COMMENT]]])
  | '*' [tfpdef] (',' [TYPE_COMMENT] tfpdef ['=' test])* (TYPE_COMMENT | [',' [TYPE_COMMENT] ['**' tfpdef [','] [TYPE_COMMENT]]])
  | '**' tfpdef [','] [TYPE_COMMENT]]] )
|  (tfpdef ['=' test] (',' [TYPE_COMMENT] tfpdef ['=' test])* (TYPE_COMMENT | [',' [TYPE_COMMENT] [
   '*' [tfpdef] (',' [TYPE_COMMENT] tfpdef ['=' test])* (TYPE_COMMENT | [',' [TYPE_COMMENT] ['**' tfpdef [','] [TYPE_COMMENT]]])
  | '**' tfpdef [','] [TYPE_COMMENT]]])
  | '*' [tfpdef] (',' [TYPE_COMMENT] tfpdef ['=' test])* (TYPE_COMMENT | [',' [TYPE_COMMENT] ['**' tfpdef [','] [TYPE_COMMENT]]])
  | '**' tfpdef [','] [TYPE_COMMENT])
)

tfpdef: NAME [':' test]


``` 
