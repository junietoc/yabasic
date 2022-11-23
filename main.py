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
    'ID'
]

reserved = {
    'LET' :'DECL'
 }

tokens += list(reserved.values())

# Regular expression rules for simple tokens
t_NUMBER = r'[0-9]+\s'
t_INT = r'[0-9]+'
t_OP = r'\+|-'
t_ASSIGN = r'='


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
lexer = lex.lex()

# Test it out
data = "10 LET X = 4"

# Give the lexer some input
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)