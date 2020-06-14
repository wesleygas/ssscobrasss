from lexer import Lexer
from parser import Parser
from symboltable import SymbolTable
import sys

if(len(sys.argv) < 2):
    raise Exception("You must provide a file to run.")


with open(sys.argv[1]) as f:
    entrada = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(entrada)
pg = Parser()
pg.parse()
parser = pg.getParser()
st = SymbolTable(name='root')
ast = parser.parse(tokens)
ast.eval(st)

