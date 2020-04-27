from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Block, Ident, PowNode
from ast import Positive, Invert, Mult, Div, Less, Greater, Equal
from ast import Assign, ReturnNode, NoOp, Negate, And, Or
from ast import IfNode, WhileNode, FuncCall, FuncDef, ArgList, Program
import lexer

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            lexer.tokenDict.keys(),
            precedence=[
                ('left', ['comp']),
                ('left', ['print'])
            ]
        )

    def parse(self):

        @self.pg.production('program : program block')
        def p_program(tokens):
            tokens[0].addChild(tokens[1])
            return tokens[0]
        
        @self.pg.production('program : block')
        def p_first_program(tokens):
            return Program(tokens[0])

        @self.pg.production('block : block stmt')
        def p_block(tokens):
            tokens[0].addChild(tokens[1])
            return tokens[0]
        
        @self.pg.production('block : stmt')
        def p_first_block(tokens):
            return Block(tokens[0])

        @self.pg.production('funccall : NAME LPAR callargs RPAR')
        def p_funccall(tokens):
            return FuncCall(tokens[0].getstr(), tokens[2].getArgs())

        @self.pg.production('funccall : NAME LPAR RPAR')
        def p_mono_funccall(tokens):
            return FuncCall(tokens[0].getstr(),[])

        @self.pg.production('callargs : callargs COMMA test')
        def p_callargs(tokens):
            tokens[0].addChild(tokens[2])
            return tokens[0]

        @self.pg.production('callargs : test')
        def p_mono_callargs(tokens):
            return ArgList(tokens[0])
        
        @self.pg.production('funcdef : DEF NAME LPAR defargs RPAR SBLK block ZBLK')
        def p_funcdef(tokens):
            return FuncDef(tokens[1].getstr(),tokens[3].getArgs(),tokens[6])
        
        @self.pg.production('funcdef : DEF NAME LPAR RPAR SBLK block ZBLK')
        def p_mono_funcdef(tokens):
            return FuncDef(tokens[1].getstr(),[],tokens[5])
            

        @self.pg.production('defargs : defargs COMMA NAME')
        def p_defargs(tokens):
            tokens[0].addChild(tokens[2].getstr())
            return tokens[0]

        @self.pg.production('defargs : NAME')
        def p_mono_defargs(tokens):
            return ArgList(tokens[0].getstr())
        
        
        @self.pg.production('stmt : funcdef')
        @self.pg.production('stmt : print')
        @self.pg.production('stmt : assignment')
        @self.pg.production('stmt : if_stmt')
        @self.pg.production('stmt : while_stmt')
        @self.pg.production('stmt : return_stmt')
        @self.pg.production('stmt : test')
        def p_stmt(tokens):
            return tokens[0]

        @self.pg.production('while_stmt : WHILE test SBLK block ZBLK')
        def p_while_stmt(tokens):
            condition = tokens[1]
            blocktrue = tokens[3]
            return WhileNode(condition, blocktrue)
        

        @self.pg.production('if_stmt : IF test SBLK block ZBLK')
        def p_if_stmt(tokens):
            condition = tokens[1]
            blocktrue = tokens[3]
            return IfNode(condition, blocktrue)
        
        @self.pg.production('if_stmt : IF test SBLK block ZBLK ELSE SBLK block ZBLK')
        def p_ifelse_stmt(tokens):
            condition = tokens[1]
            blocktrue = tokens[3]
            blockfalse = tokens[7]
            return IfNode(condition, blocktrue, blockfalse)

        @self.pg.production('return_stmt : RETURN test')
        def p_return_stmt(tokens):
            return ReturnNode(tokens[1])

        @self.pg.production('return_stmt : RETURN')
        def p_mono_return_stmt(tokens):
            return ReturnNode(NoOp())

        @self.pg.production('assignment : NAME EQUAL test')
        def p_assignment(tokens):
            left = tokens[0].getstr()
            right = tokens[2] 
            return Assign(left, right)

        @self.pg.production('print : PRINT LPAR test RPAR')
        def p_print(tokens):
            return Print(tokens[2])
        
        @self.pg.production('atom : NUMBER')
        @self.pg.production('atom : NAME')
        def p_atom(tokens):
            token = tokens[0]
            if(token.gettokentype() == 'NUMBER'):
                return Number(int(token.getstr()))
            elif(token.gettokentype() == 'NAME'):
                return Ident(token.getstr())
        
        @self.pg.production('atom : funccall')
        def p_func_atom(tokens):
            return tokens[0]
        

        @self.pg.production('power : atom')        
        def p_mono_power(tokens):
            return tokens[0]

        @self.pg.production('power : atom STARSTAR factor')
        def p_power(tokens):
            left = tokens[0]
            right = tokens[2]
            return PowNode(left, right)
        
        @self.pg.production('factor : PLUS factor')
        @self.pg.production('factor : MINUS factor')  
        def p_factor(tokens):
            sign = tokens[0].gettokentype()
            symb = tokens[1]
            if(sign == 'PLUS'):
                return Positive(symb)
            elif(sign == 'MINUS'):
                return Invert(symb)
            else:
                raise Exception(f"{tokens} passaram liso")

        @self.pg.production('factor : power') 
        def p_mono_factor(tokens):
            return tokens[0]
        
        @self.pg.production('term : factor STAR factor')
        @self.pg.production('term : factor SLASH factor')
        def p_term(tokens):
            op = tokens[1].gettokentype()
            left = tokens[0]
            right = tokens[2]
            if(op == 'STAR'):
                return Mult(left,right)
            if(op == 'SLASH'):
                return Div(left,right)
            else:
                raise Exception(f"{tokens} passaram liso")
        
        @self.pg.production('term : factor')
        def p_mono_term(tokens):
            return tokens[0]


        @self.pg.production('expr : term PLUS term')
        @self.pg.production('expr : term MINUS term')
        def p_expr(tokens):
            op = tokens[1].gettokentype()
            left = tokens[0]
            right = tokens[2]
            if(op == 'PLUS'):
                return Sum(left,right)
            if(op == 'MINUS'):
                return Sub(left,right)
            else:
                raise Exception(f"{tokens} passaram liso")
        
        @self.pg.production('expr : term')
        def p_mono_expr(tokens):
            return tokens[0]
        
        @self.pg.production('comp : expr LESS expr')
        @self.pg.production('comp : expr GREATER expr')
        @self.pg.production('comp : expr EQEQUAL expr')
        def p_comp(tokens):
            op = tokens[1].gettokentype()
            left = tokens[0]
            right = tokens[2]
            if(op == 'LESS'):
                return Less(left, right)
            elif(op == 'GREATER'):
                return Greater(left,right)
            elif(op == 'EQEQUAL'):
                return Equal(left, right)

        @self.pg.production('comp : expr')
        def p_mono_comp(tokens):
            return tokens[0]

        @self.pg.production('not_test : NOT not_test')
        def p_not_test(tokens):
            return Negate(tokens[1])

        @self.pg.production('not_test : comp')
        def p_mono_not_test(tokens):
            return tokens[0]

          
        @self.pg.production('and_test : not_test  AND  not_test')
        @self.pg.production('and_test : and_test  AND  not_test')
        def p_and_test(tokens):
            return And(tokens[0], tokens[2])

        @self.pg.production('and_test : not_test')
        def p_mono_and_test(tokens):
            return tokens[0]

        @self.pg.production('or_test : and_test  OR  and_test')
        @self.pg.production('or_test : or_test  OR  and_test')
        def p_or_test(tokens):
            return Or(tokens[0], tokens[2])

        @self.pg.production('or_test : and_test')
        def p_mono_or_test(tokens):
            return tokens[0]
        
        @self.pg.production('test : or_test')
        def p_mono_test(tokens):
            return tokens[0]

        
        @self.pg.error
        def error_handle(token):
            raise ValueError("Ran into a %s in where it wasn't expected" % token.gettokentype())
    
    def getParser(self):
        return self.pg.build()           