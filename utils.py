RAW_TOKENS = [
    'NUMBER',
    'INT',
    'OP',
    'VAR',
    'ASSIGN',
    'STRING',
    'ID',
    'SEP',
    'B'
]

RESERVED = {
    'LET' :'LET',
    'GOTO':'GOTO',
    'END':'END',
    'PRINT':'PRINT'
 }

TOKENS = RAW_TOKENS + list(RESERVED.values())