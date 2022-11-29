from BasicLexer import basic_lexer
from BasicParser import basic_parser

mylexer = basic_lexer()
myparser = basic_parser()

debug = False
""" myparser.parser.parse(input="10 LET XOA=3+12", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="11 LET WA=1", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="12 LET AAGF=2", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="13 LET BA=3", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="20 LET YA=4-12-XOA", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="21 LET ZA=XOA+YA-2-6+8", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="23 PRINT XOA,WA", lexer=mylexer.lexer, debug=debug)
myparser.parser.parse(input="30 PRINT XOA,YA,ZA,WA,AAGF,BA", lexer=mylexer.lexer, debug=debug)
 """
myparser.parser.parse(input="10 PRINT \"HomE\"", lexer=mylexer.lexer, debug=False)
myparser.parser.parse(input="20 PRINT \"sweet\"", lexer=mylexer.lexer, debug=False)