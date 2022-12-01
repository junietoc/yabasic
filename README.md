# YA' BASIC: Un intérprete básico de BASIC en Python
Este repositorio contiene el proyecto final para la clase de Compiladores 2022-II realizado por 
- Santiago Tovar Mosquera
- Juliana Alejandra Nieto Cárdenas

### ¿Cómo funciona este intérprete?
YA' BASIC soporta funciones de asignación, aritmética básica con suma y resta, impresión de variables y la función insignia de algunos de los primeros lenguajes de programación: `GOTO`

#### Comandos soportados por YA' BASIC
- Asignación y re-asignación como: 
```
10 LET X = 2
20 X = 4
```

- Operaciones matemáticas con suma y resta (sin usar paréntesis)
```
10 LET X = 3-4
20 LET Y = 
```

- Impresión de variables

Esta puede realizarse, imprimiendo una sola variable, múltiples variabels (usando comas) o imprimiendo cadenas (usando comillas dobles)
```
...
30 PRINT X
40 PRINT A,B
50 PRINT "HELLO WORLD"
```

- Función `GOTO`
Este comando sirve para saltar líneas de código hacia la inidicada con `GOTO`
```
10 PRINT "HOME"
20 PRINT "SWEET"
30 GOTO 10
```

#### Para ejecutar
Sólo hace falta escribir el comando `RUN` al finalizar de escribir las líneas de código 

### ¿Cómo instalar?
Las siguientes instrucciones pueden ser exitosamente ejecutadas en `Git Bash`
1. Clonar el repositorio
```git clone https://github.com/junietoc/yabasic.git```
2. Acceder a la carpeta del repositorio local
```
cd yabasic/
```
3. Crear ambiente virtual
```
pip3 -m venv myenv
```

4. Activar ambiente virtual
```
source myenv/bin/activate
```

5. Instalar paquetes necesarios
```
pip install -r requirements.txt
```
6. ***Ejecutar intérprete***
```
python Program.py
```
### Algunos ejemplos listos para ejecutarse en YA' BASIC
1. El clásico de futurama
```
10 PRINT "HOME"
20 PRINT "SWEET"
30 GOTO 10
RUN
```

2. Asignaciones y reasignaciones
```
10 LET X = 1
20 LET Y = 2
30 X = X+Y
40 PRINT Y,X
RUN
```

3. Saltando impresiones
```
10 PRINT "HELLO WORLD"
20 PRINT "SKIPPING THIS LINE"
15 GOTO 30
30 PRINT "THE END"
RUN
```