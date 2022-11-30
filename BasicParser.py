import ply.yacc as yacc


from utils import TOKENS, RESERVED


def index_hasta_sep(cad,inicio):
    ind=inicio
    while(cad[ind]!="SEP"):
        ind+=1
    return ind 

def index_hasta_coma(cad,inicio):
    ind=inicio
    while(ind<len(cad) and cad[ind]!=","):
        ind+=1
    return ind 

class basic_parser():
    tokens = TOKENS
    goto_index=-1
    

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
        try:
            if (len(p) == 2):
                p[0] = p[1]
            else:
                p[0] = int(p[1]) + int(p[2])
        except:
            self.p_error(p)



    def p_statement(self,p):
        '''s : NUMBER LET VAR ASSIGN expr
             | NUMBER GOTO INT'''
        if(len(p)==6):
            if (isinstance(p[5],int)):
                self.vars[p[3]] = p[5]
            else:
                self.p_error(p)
        else:
            self.goto_index=int(p[3])

    def p_reassign(self,p):
        '''s : NUMBER VAR ASSIGN expr'''
        if(p[2] in self.vars):
            self.vars[p[2]]=p[4]
        else:
            self.p_error(p)
     
    def p_print_string(self,p):
        '''s : NUMBER PRINT STRING'''
        print(p[3][1:len(p[3])-1])   
    

    
    def p_empty(self,p):
        'empty :'
        pass
   

    def p_varprint(self,p):
        '''varprint : VAR SEP VAR
                    | varprint SEP VAR'''
        if(len(p)==4):     
            p[0]=p[1]+","+p[3]
        else:
            p[0]=""
            for cont in range(len(p)):
                for i in range(cont,index_hasta_sep(p,cont)):
                    p[0]=p[0]+p[i]
                p[0]=p[0]+","
                cont=i+1    
 


    def p_print(self,p):
        '''s : NUMBER PRINT VAR
             | NUMBER PRINT varprint'''
        # printing just one variable
        try:
            if ("," not in p[3]):
                p[0] = str(self.vars[p[3]])
                print(self.vars[p[3]])
            else:
                varImprimir = list()
                cont = 0
                while (cont < len(p[3])):
                    variablelist = list()
                    for i in range(cont, index_hasta_coma(p[3], cont)):
                        a = p[3][i]
                        variablelist.append(a)
                    variable = "".join(e for e in variablelist)
                    varImprimir.append(variable)
                    cont = index_hasta_coma(p[3], cont) + 1
                x = ",".join([str(self.vars[e]) for e in varImprimir])
                p[0] = str(x)
                print(x)
        except:
            self.p_error(p)

    def p_error(self,p):
        try:
            p[0] = f"error in line {p[1]}"

        except:
            print("Syntax Error")

    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.vars = dict()