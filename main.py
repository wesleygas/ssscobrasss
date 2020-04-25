from lexer import Lexer

with open('test_med.txt') as f:
    entrada = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(entrada)

for token in tokens:
    print(token)