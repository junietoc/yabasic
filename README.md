# YA' BASIC: Un intérprete básico de BASIC en Python
Este repositorio contiene el proyecto final para la clase de Compiladores 2022-II realizado por 
- Santiago Tovar Mosquera
- Juliana Alejandra Nieto Cárdenas

### ¿Cómo funciona este intérprete?
YA' BASIC soporta funciones de asignación, aritmética básica con suma y resta, impresión de variables y la función insignia de algunos de los primeros lenguajes de programación: `GOTO`

#### Comandos soportados por YA' BASIC
- Asignación y re-asignación como: 
'''
10 LET X = 2
20 X = 4
'''

- Operaciones matemáticas con suma y resta (sin usar paréntesis)
'''
10 LET X = 3-4
20 LET Y = 
'''

- Impresión de variables

Esta puede realizarse, imprimiendo una sola variable, múltiples variabels (usando comas) o imprimiendo cadenas (usando comillas dobles)
'''
...
30 PRINT X
40 PRINT A,B
50 PRINT "HELLO WORLD"
'''

- Función `GOTO`
Este comando sirve para saltar líneas de código hacia la inidicada con `GOTO`
'''
10 PRINT "HOME"
20 PRINT "SWEET"
30 GOTO 10
'''

### ¿Cómo instalar?
`git clone https://github.com/junietoc/yabasic.git`
