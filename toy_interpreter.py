from BasicLexer import basic_lexer
from BasicParser import basic_parser

mylexer = basic_lexer()
myparser = basic_parser()

debug = True
myparser.parser.parse(input="10 LET X=3+1", lexer=mylexer.lexer, debug=debug)

myparser.parser.parse(input="20 PRINT X", lexer=mylexer.lexer, debug=debug)
