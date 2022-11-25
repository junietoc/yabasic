# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
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

reserved = {
    'LET' :'LET',
    'GOTO':'GOTO',
    'END':'END',
    'PRINT':'PRINT'
 }

tokens += list(reserved.values())

# Regular expression rules for simple tokens
t_NUMBER = r'[0-9]+\s'
t_INT = '[0-9]+'
t_OP = r'\+|-'
t_ASSIGN = r'='
t_STRING = r'"[a-z0-9]+"'
t_SEP = r'\,'
t_B =r'\n'


def t_VAR(t):
    r'[A-Z]+'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer


# Test it out
data = ['10 LET X=1',
'20 LET Y=X+3',
'30 PRINT X,Y',
'31 GOTO 38',
'35 PRINT "hello"',
'36 GOTO 40',
'38 PRINT "paso1"',
'39 GOTO 35',
'40 END',
]

# Give the lexer some input
for line in data:
    lexer = lex.lex()
    lexer.input(line)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

