from BasicLexer import basic_lexer
from BasicParser import basic_parser

mylexer = basic_lexer()
myparser = basic_parser()

debug = True
myparser.parser.parse(input="10 LET X=3+12", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="20 LET Y=4-12+X", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="21 LET Z=X+Y-2-6+8", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="23 PRINT Y", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="30 PRINT X,Z", lexer=mylexer.lexer, debug=debug)
