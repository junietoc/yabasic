import ply.yacc as yacc


from utils import TOKENS, RESERVED

class basic_parser():
    tokens = TOKENS

    

    def p_program(self,p):
        'c : s'
        p[0]=p[1]



    def p_value(self,p):
        '''value : VAR
                 | INT'''
        if p[1] in self.vars.keys():
            p[0] = self.vars[p[1]]
        else:
            p[0] = p[1]


    def p_term(self,p):
        '''term : OP value
                | term term 
                | empty'''  
        if(p[1]=='+' or p[1]=='-'):
            if(p[1]=='+'):
                p[0]=int(p[2])
            if(p[1]=='-'):
                p[0]=-int(p[2])
        elif(len(p)==3):
            p[0]=0
            for i in range(len(p)):
                p[0]+=p[i]
        else:
            pass


    def p_expr(self,p):
        '''expr : value 
                | value term'''
        if(len(p)==2):
            p[0] = p[1]
        else:
            p[0] = int(p[1])+int(p[2])    


    def p_statement(self,p):
        's : NUMBER LET VAR ASSIGN expr'
        self.vars[p[3]] = p[5]
    
    def p_empty(self,p):
        'empty :'
        pass

    def p_print(self,p):
        's : NUMBER PRINT VAR'
        print(self.vars[p[3]])


    def p_error(self,p):
        print(p)
        print("Syntax error in input!")

    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.vars = dict()