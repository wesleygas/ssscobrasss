from rply import LexerGenerator
import re

tokenDict = {
    'PRINT': r'print',
    'WHILE': r'while',
    'RETURN': r'return',
    'DEF':r'def',
    'IF': r'if',
    'ELIF': r'elif',
    'ELSE': r'else',
    'RETURN': r'return',
    'NUMBER': r'\d+',
    'LPAR': r'\(',
    'RPAR': r'\)',
    'SBLK': r'sss',
    'ZBLK': r'zzz',
    'NAME': r'[a-z]\w*',
    'COMMA':r'\,',
    'SEMI':r'\;',
    'PLUS':r'\+',
    'MINUS':r'\-',
    'STARSTAR': r'\*\*',
    'STAR': r'\*',
    'SLASH': r'\/',
    'LESS': r'\<',
    'GREATER': r'\>',
    'EQEQUAL': r'\=\=',
    'EQUAL': r'\=',
    'NOT': r'\!', #lembrando q o not eh igual a c pq sim
    'AND': r'\&\&',
    'OR' : r'\|\|',
}

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        for name, reg in tokenDict.items():
            print("compiling: ", name)
            self.lexer.add(name, reg, flags=re.IGNORECASE)
        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'\n+')
        self.lexer.ignore(r'\t+')
    
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()