from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Block, Ident, PowNode, Positive, Negate, Mult, Div
import lexer

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            lexer.tokenDict.keys()
        )

    def parse(self):
        @self.pg.production('program : PRINT LPAR expr RPAR')
        def program(p):
            return Print(p[2])
        
        @self.pg.production('atom : NUMBER')
        @self.pg.production('atom : NAME')
        def p_atom(tokens):
            token = tokens[0]
            if(token.gettokentype() == 'NUMBER'):
                return Number(int(token.getstr()))
            elif(token.gettokentype() == 'NAME'):
                return Ident(token)

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
            terma = tokens[0]
            termb = tokens[2]
            if(op == 'STAR'):
                return Mult(terma,termb)
            if(op == 'SLASH'):
                return Div(terma,termb)
            else:
                raise Exception(f"{tokens} passaram liso")
        
        @self.pg.production('term : factor')
        def p_mono_term(tokens):
            return tokens[0]


        @self.pg.production('expr : term PLUS term')
        @self.pg.production('expr : term MINUS term')
        def p_expr(tokens):
            op = tokens[1].gettokentype()
            terma = tokens[0]
            termb = tokens[2]
            if(op == 'PLUS'):
                return Sum(terma,termb)
            if(op == 'MINUS'):
                return Sub(terma,termb)
            else:
                raise Exception(f"{tokens} passaram liso")
        
        @self.pg.production('expr : term')
        def p_mono_expr(tokens):
            return tokens[0]
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)
    
    def getParser(self):
        return self.pg.build()

                