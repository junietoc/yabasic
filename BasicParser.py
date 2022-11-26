import ply.yacc as yacc


from utils import TOKENS, RESERVED

class basic_parser():
    tokens = TOKENS


    def p_program(self,p):
        'c : s'
        p[0]=p[1]



    def p_value(self,p):
        'value : INT'
        '   | VAR'
        if p[1] in self.vars.keys():
            p[0] = self.vars[p[1]]
        else:
            p[0] = p[1]


    def p_term(self,p):
        'term : value OP value'
        if(p[2]=="+"):
            p[0]=p[1]+p[3]
        else:
            p[0] = p[1] - p[3]
    def p_expr(self,p):
        'expr : value'
        '   | term'
        p[0] = p[1]
    def p_statement(self,p):
        's : NUMBER LET VAR ASSIGN expr'
        self.vars[p[3]] = p[5]


    def p_print(self,p):
        's : NUMBER PRINT VAR'
        print(p[0])
        print(self.vars[p[3]])


    def p_error(self,p):
        print(p)
        print("Syntax error in input!")

    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.vars = dict()