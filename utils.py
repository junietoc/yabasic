# tokens no terminales usandos en la gramática
RAW_TOKENS = [
    'NUMBER',
    'INT',
    'OP',
    'VAR',
    'ASSIGN',
    'STRING',
    'SEP'
]
# palabras reservadas que son tokens terminales usandos en la gramática
RESERVED = {
    'LET' :'LET',
    'GOTO':'GOTO',
    'PRINT':'PRINT'
 }

# lista de tokens que incluye las palabras reservadas
TOKENS = RAW_TOKENS + list(RESERVED.values())