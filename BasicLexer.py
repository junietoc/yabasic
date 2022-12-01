import ply.lex as lex
from utils import TOKENS, RESERVED

class basic_lexer():
    #Obtenemos los tokens a partir del archivo utils donde fueron definidos
    tokens = TOKENS

    #Específicamos las regular expressions para la mayoría de los tokens
    t_NUMBER = r'[0-9]+\s'          #Representa la numeración de cada línea de código, por eso es un entero seguido de un espacio
    t_INT = '[0-9]+'                #Un numero entero
    t_OP = r'\+|-'                  #Operaciones aritméticas válidas
    t_ASSIGN = r'='                 #Simbolo de igualadad para la asignación
    t_SEP = r'\,'                   #Símbolo de coma para la separación de variables


    #Definimos el token STRING mediante una función para garantizar que la STRING ingresada no haga parte de las palabras reservadas
    def t_STRING(self,t):
        r'"([a-z|A-Z|0-9]+\s*[a-z|A-Z|0-9]*)+"'     #Definimos en primera instancia el token mediante su regular expression
                                                    #Al menos un carácter, seguido de un posible espacio con más carácteres. Todo esto al menos una vez
        reserved=RESERVED                           #Llamamos a las palabras reservadas
        t.type = reserved.get(t.value,'STRING')     #Revisamos que STRING no esté en ellas
        return t

    #Definimos el token VAR mediante una función para garantizar que la VAR ingresada no haga parte de las palabras reservadas
    def t_VAR(self,t):
        r'[A-Z]+'                               #Definimos el token con su regular expresion
                                                #Al menos una letra en mayúscula 
        reserved = RESERVED                     #Llamamos a las palabras reservadas
        t.type = reserved.get(t.value, 'VAR')   #Revisamos que VAR no esté en ellas
        return t

    #Ingresamos los tokens que ignoraremos, en este caso tab
    t_ignore = ' \t'

    #La función error identifica cuando un carácter no coincide con ninguno de los tokens propuestos e imprime el error
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    #Testea un input y extrae los tokens de la misma
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


    
    def __init__(self):
        self.lexer = lex.lex(module=self)

