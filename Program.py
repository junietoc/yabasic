from BasicLexer import basic_lexer
from BasicParser import basic_parser
import re

class program:
    def __init__(self):
        self.lineas = list("")
        self.mylexer = basic_lexer()
        self.myparser = basic_parser()

    def execute(self):
        line=input()
        while(line!="RUN"):
            number_line=int(re.findall('[0-9]+\s', line)[0])
            self.agregar_lineas(line,number_line)
            line=input()
        for e in self.lineas:
            if(e!=''):
                self.myparser.parser.parse(input=e, lexer=self.mylexer.lexer)
                


    def agregar_lineas(self,linea,num):
        if(num<len(self.lineas)):
            self.lineas[num]=linea
        else:
            for i in range(len(self.lineas),num):
                self.lineas.append("")
            self.lineas.append(linea)    


p=program()
p.execute()            

