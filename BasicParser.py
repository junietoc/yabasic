import ply.yacc as yacc


from utils import TOKENS, RESERVED

# funcion para encontrar el token SEP en una cadena desde un indice inicial
def index_hasta_sep(cad,inicio):
    ind=inicio
    while(cad[ind]!="SEP"):
        ind+=1
    return ind 

# funcion para encontrar el valor del token SEP "," en una cadena desde un indice inicial
def index_hasta_coma(cad,inicio):
    ind=inicio
    while(ind<len(cad) and cad[ind]!=","):
        ind+=1
    return ind 

# clase para basic_parser
class basic_parser():
    # lista de TOKENS incluye palabras reservadas desde utils.py
    tokens = TOKENS
    # indice al cual dirigir la sentencia GOTO
    goto_index=-1

    # GRAMÁTICA
    # en cada función se define la regla por medio de una docstring
    # la función ejecuta las acciones que pueda presentar cada caso de la regla

    # función para la primer regla, donde c es el símbolo inicial de la gramática
    # Rule 1     c -> s
    def p_program(self,p):
        'c : s'
        # se aplica la regla
        p[0]=p[1]


    # función para el no termina value
    #
    # Rule 2     value -> VAR
    # Rule 3     value -> INT
    def p_value(self,p):
        '''value : VAR
                 | INT'''
        # caso: VAR
        if p[1] in self.vars.keys():
            # se verifica que la variable este guardada en memoria y si es el caso se aplica la regla
            p[0] = self.vars[p[1]]
        # caso: INT
        else:
            p[0] = p[1]

    # función para el no terminal term
    # esta función ejecuta las operaciones artiméticas
    # Rule 4     term -> OP value
    # Rule 5     term -> term term
    # Rule 6     term -> empty
    def p_term(self,p):
        '''term : OP value
                | term term 
                | empty'''
        # caso: OP value
        # verifica si hay un token de operación
        if(p[1]=='+' or p[1]=='-'):
            if(p[1]=='+'):
                # si encuentra el símbolo de suma, guarda entero
                p[0]=int(p[2])
            if(p[1]=='-'):
                # si encuentra el símbolo de suma, guarda el opuesto aditivo de entero
                p[0]=-int(p[2])
        # caso: term term
        elif(len(p)==3):
            p[0]=0
            # se ejecutan las operaciones recorriendo los terminos y acumulando la suma
            # se guarda esta suma
            for i in range(len(p)):
                p[0]+=p[i]
        else:
            pass

    # función para el no termina expr
    # esta función asigna valores y opera de manera binaria
    # Rule 7     expr -> value
    # Rule 8     expr -> value term
    def p_expr(self,p):
        '''expr : value 
                | value term'''
        try:
            # caso: value
            if (len(p) == 2):
                p[0] = p[1]
            # caso: value term
            else:
                p[0] = int(p[1]) + int(p[2])
        except:
            # captura el error de si se quiere operar valores no numéricos
            self.p_error(p)


    # función para s
    # esta función asigna valores a variables
    # Rule 9     s -> NUMBER LET VAR ASSIGN expr
    # Rule 10    s -> NUMBER GOTO INT
    def p_statement(self,p):
        '''s : NUMBER LET VAR ASSIGN expr
             | NUMBER GOTO INT'''

        # caso: NUMBER LET VAR ASSIGN expr
        if(len(p)==6):
            # en el caso que la expr es un entero producto de una operación aritmética
            if (isinstance(p[5],int)):
                self.vars[p[3]] = p[5]
            else:
                # si el valor a asignar es un entero que se recibe como str
                if p[5].isnumeric():
                    self.vars[p[3]] = p[5]
                else:
                    # captura errores en caso que el valor sea no numérico
                    self.p_error(p)
        else:
            # caso: GOTO INT
            self.goto_index=int(p[3])

    # función para re asignar valores a variables
    # Rule 11    s -> NUMBER VAR ASSIGN expr
    def p_reassign(self,p):
        '''s : NUMBER VAR ASSIGN expr'''

        if(p[2] in self.vars):
            # caso para asignar entero producto de operación aritmética
            if (isinstance(p[4], int)):
                self.vars[p[2]]=p[4]
                # si el valor a asignar es un entero que se recibe como str
                if p[4].isnumeric():
                    self.vars[p[2]] = p[4]
                else:
                    # captura errores en caso que el valor sea no numérico
                    self.p_error(p)
            else:
                # captura errores en caso que el valor sea no numérico
                self.p_error(p)
        else:
            # captura errores en caso que el valor sea no numérico
            self.p_error(p)

    # función para s
    # esta función imprime cadenas
    # Rule 12    s -> NUMBER PRINT STRING
    def p_print_string(self,p):
        '''s : NUMBER PRINT STRING'''
        print(p[3][1:len(p[3])-1])   
    

    # función para la regla vacía
    # se ejecuta cuando se llama emtpy como un no terminal
    # Rule 13    empty -> <empty>
    def p_empty(self,p):
        'empty :'
        pass
   
    # función para el no terminal varprint
    # concatena valores, sean enteros o variables con comas
    # Rule 14    varprint -> VAR SEP VAR
    # Rule 15    varprint -> varprint SEP VAR
    def p_varprint(self,p):
        '''varprint : VAR SEP VAR
                    | varprint SEP VAR'''
        # caso: VAR SEP VAR
        if(len(p)==4):     
            p[0]=p[1]+","+p[3]
        else:
            # caso: varprint SEP VAR
            p[0]=""
            # se itera por los posibles var print para concatenar valores con comas
            for cont in range(len(p)):
                for i in range(cont,index_hasta_sep(p,cont)):
                    p[0]=p[0]+p[i]
                p[0]=p[0]+","
                cont=i+1    
 

    # función para s
    # imprime valores en consola
    # Rule 16    s -> NUMBER PRINT VAR
    # Rule 17    s -> NUMBER PRINT varprint
    def p_print(self,p):
        '''s : NUMBER PRINT VAR
             | NUMBER PRINT varprint'''
        try:
            # caso NUMBER PRINT VAR
            if ("," not in p[3]):
                p[0] = str(self.vars[p[3]])
                # imprime VAR
                print(self.vars[p[3]])
            else:
                # caso NUMBER PRINT varprint
                varImprimir = list()
                cont = 0
                # itera por varprint encontrando comas y variables para luego imprimir una sola cadena con toda esta información
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
            # captura error de imprimir variables que no han sido definidas
            self.p_error(p)

    # función para capturar errores de sintáxis
    def p_error(self,p):
        try:
            p[0] = f"error in line {p[1]}"

        except:
            print("Syntax Error")

    # constructor del parser con la inicialización de la memoria
    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.vars = dict()