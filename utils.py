RAW_TOKENS = [
    'NUMBER',
    'INT',
    'OP',
    'VAR',
    'ASSIGN',
    'STRING',
    'SEP'
]

RESERVED = {
    'LET' :'LET',
    'GOTO':'GOTO',
    'PRINT':'PRINT'
 }

TOKENS = RAW_TOKENS + list(RESERVED.values())