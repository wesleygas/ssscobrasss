from lexer import Lexer

entrada = """
    print(1);
    loga = 3;
    logb = loga + 4;
    while(!(logb == loga))sss
        loga = loga + 1;
    zzzelsesss
        print(loga);
        print(logb);
    zzz

    def aloha(a1,a2,a3)sss
        print(a1);
        print(0);
        print(a2);
        print(1);
        print(a3);
    zzz

    aloha(loga,logb,3);

"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(entrada)

for token in tokens:
    print(token)