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

            result = self.agregar_lineas(line)
            if result == "error":
                break
            line=input()
        i=0
        while (i<len(self.lineas)):
            e=self.lineas[i]
            if(e!=''):
                result = self.myparser.parser.parse(input=e, lexer=self.mylexer.lexer)
                if(self.myparser.goto_index!=-1):
                    i=self.myparser.goto_index-1
                    self.myparser.goto_index=-1
                if result:
                    if ("error" in result):
                        print(result)
                        break
            i+=1




    def agregar_lineas(self,line):
        list_found_num = re.findall('[0-9]+\s', line)
        if len(list_found_num) > 0:
            num = int(re.findall('[0-9]+\s', line)[0])

            if (num < len(self.lineas)):
                self.lineas[num] = line
            else:
                for i in range(len(self.lineas), num):
                    self.lineas.append("")
                self.lineas.append(line)
        else:
            print("error")
            return "error"


p=program()
p.execute()