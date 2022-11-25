import ply.yacc as yacc


from utils import TOKENS, RESERVED

class basic_parser():
    tokens = TOKENS


    def p_program(self,p):
        'c : s'
        p[0]=p[1]


    def p_statement(self,p):
        's : NUMBER LET VAR ASSIGN q'
        self.vars[p[3]] = p[5]
    def p_print(self,p):
        's : NUMBER PRINT VAR'
        print(self.vars[p[3]])


    def p_error(self,p):
        print("Syntax error in input!")
    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.vars = dict()