from lexer import Lexer
from parser import Parser
from symboltable import SymbolTable
with open('test_simpl.txt') as f:
    entrada = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(entrada)

pg = Parser()
pg.parse()
parser = pg.getParser()
st = SymbolTable(name='root')
parser.parse(tokens).eval(st)

