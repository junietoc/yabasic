from BasicLexer import basic_lexer
from BasicParser import basic_parser

mylexer = basic_lexer()
myparser = basic_parser()

print(myparser.parser.parse(input="10 LET X = 71", lexer=mylexer.lexer))
print(myparser.parser.parse(input="20 PRINT X", lexer=mylexer.lexer))