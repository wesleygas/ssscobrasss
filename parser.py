from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Block, Ident, PowNode
from ast import Positive, Negate, Mult, Div, Less, Greater, Equal
from ast import Assign, ReturnNode, NoOp
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

        @self.pg.production('block : block stmt')
        def p_block(tokens):
            tokens[0].addChild(tokens[1])
            return tokens[0]
        
        @self.pg.production('block : stmt')
        def p_first_block(tokens):
            return Block(tokens[0])

        #@self.pg.production('stmt : if_stmt')
        #@self.pg.production('stmt : return_stmt')
        @self.pg.production('stmt : comp')
        @self.pg.production('stmt : print')
        @self.pg.production('stmt : assignment')
        def p_stmt(tokens):
            return tokens[0]

        #@self.pg.production('if_stmt : IF test SBLK suit ZBLK')
        #def p_if_stmt(tokens):
        #    return


        #@self.pg.production('return_stmt : RETURN comp')
        #def p_return_stmt(tokens):
        #    return ReturnNode(tokens[1])

        #@self.pg.production('return_stmt : RETURN')
        #def p_mono_return_stmt(tokens):
        #    return ReturnNode(NoOp())

        @self.pg.production('assignment : NAME EQUAL comp')
        def p_assignment(tokens):
            left = tokens[0].getstr()
            right = tokens[2] 
            return Assign(left, right)

        @self.pg.production('print : PRINT LPAR comp RPAR')
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
                return Negate(symb)
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

        
        @self.pg.error
        def error_handle(token):
            raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())
    
    def getParser(self):
        return self.pg.build()

                