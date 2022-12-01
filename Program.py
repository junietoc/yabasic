from BasicLexer import basic_lexer
from BasicParser import basic_parser
import re

#Clase programa que ejecutará el ingreso de las lineas en BASIC
class program:
    #Constructor para la clase programa
    def __init__(self):
        self.lineas = list("")              #Atributo para guardar las lineas de codigo ingresadas
        self.mylexer = basic_lexer()        #Atributo para crear el Lexer 
        self.myparser = basic_parser()      #Atributo para crear el parser


    #Metodo de ejecución para el programa
    def execute(self):
        line=input()                            #El usuario ingresa una linea de código
        while(line!="RUN"):                     #Mientras que el usuario no ingrese "RUN" y no haya errores, permitirá ingresar más
            result = self.agregar_lineas(line)
            if result == "error":
                break
            line=input()
        i=0
        #Recorremos cada una de las líneas de código en el atributo lineas, omitiendo las vacías
        while (i<len(self.lineas)):
            e=self.lineas[i]
            if(e!=''):
                result = self.myparser.parser.parse(input=e, lexer=self.mylexer.lexer)          #Ejecutamos el parser para cada linea no vacía
                if(self.myparser.goto_index!=-1):
                    #Si la linea es un comando GOTO, el goto_index ya no será -1, así que ingresamos al if y evaluamos si el índice
                        #de la nueva línea de código es válido, es decir nos re dirige a una línea existente y no vacía
                    if(self.myparser.goto_index>=len(self.lineas) or self.lineas[self.myparser.goto_index]==''):
                        #Si el índice no es válido, no imprime el error e interrumpe la ejecución del código
                        print(f"error in line {i}")        
                        break
                    #Si el índice es válido, se reasigna al contador que recorre el arreglo lineas y se reestable el goto_index
                    i=self.myparser.goto_index-1
                    self.myparser.goto_index=-1
                #Si el parser retorna un error, se interrumpe la ejecución    
                if result:
                    if ("error" in result):
                        print(result)
                        break
            i+=1



    #El metodo agregar lineas nos permite insertar una nueva línea de código en BASIC al arreglo lineas
    def agregar_lineas(self,line):
        #Primero extraemos la numeración de la linea recién escrita
        list_found_num = re.findall('[0-9]+\s', line)
        if len(list_found_num) > 0:
            num = int(re.findall('[0-9]+\s', line)[0])
            if (num < len(self.lineas)):                    #Si la numeración es menor a la long. de la lista, entonces reemplazamos lo que esté en esa posición del arreglo
                self.lineas[num] = line
            else:
                for i in range(len(self.lineas), num):     #Si la numeración es mayor, entonces añadimos elementos vacíos a la lista hasta llegar al índice deseado
                    self.lineas.append("")
                self.lineas.append(line)
        else:
            print("error")
            return "error"


#Creamos un programa, y lo ejecutamos
p=program()
p.execute()