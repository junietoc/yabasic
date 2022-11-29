import ply.lex as lex
from utils import TOKENS, RESERVED

class basic_lexer():
    tokens = TOKENS

    t_NUMBER = r'[0-9]+\s'
    t_INT = '[0-9]+'
    t_OP = r'\+|-'
    t_ASSIGN = r'='
    t_SEP = r'\,'
    t_B = r'\n'

    def t_STRING(self,t):
        r'"([a-z|A-Z]+\s*[a-z|A-Z]*)+"'
        reserved=RESERVED
        t.type = reserved.get(t.value,'STRING')    # Check for reserved words
        return t


    def t_VAR(self,t):
        r'[A-Z]+'
        reserved = RESERVED
        t.type = reserved.get(t.value, 'VAR')  # Check for reserved words
        return t

    t_ignore = ' \t'

    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    def __init__(self):
        self.lexer = lex.lex(module=self)

