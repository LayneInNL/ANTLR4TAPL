# Generated from ./UntypedExpr.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,79,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,4,11,74,8,11,
        11,11,12,11,75,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,21,11,23,12,1,0,1,3,0,9,10,12,13,32,32,79,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,
        23,1,0,0,0,1,25,1,0,0,0,3,30,1,0,0,0,5,36,1,0,0,0,7,39,1,0,0,0,9,
        44,1,0,0,0,11,49,1,0,0,0,13,51,1,0,0,0,15,56,1,0,0,0,17,61,1,0,0,
        0,19,68,1,0,0,0,21,70,1,0,0,0,23,73,1,0,0,0,25,26,5,116,0,0,26,27,
        5,114,0,0,27,28,5,117,0,0,28,29,5,101,0,0,29,2,1,0,0,0,30,31,5,102,
        0,0,31,32,5,97,0,0,32,33,5,108,0,0,33,34,5,115,0,0,34,35,5,101,0,
        0,35,4,1,0,0,0,36,37,5,105,0,0,37,38,5,102,0,0,38,6,1,0,0,0,39,40,
        5,116,0,0,40,41,5,104,0,0,41,42,5,101,0,0,42,43,5,110,0,0,43,8,1,
        0,0,0,44,45,5,101,0,0,45,46,5,108,0,0,46,47,5,115,0,0,47,48,5,101,
        0,0,48,10,1,0,0,0,49,50,5,48,0,0,50,12,1,0,0,0,51,52,5,115,0,0,52,
        53,5,117,0,0,53,54,5,99,0,0,54,55,5,99,0,0,55,14,1,0,0,0,56,57,5,
        112,0,0,57,58,5,114,0,0,58,59,5,101,0,0,59,60,5,100,0,0,60,16,1,
        0,0,0,61,62,5,105,0,0,62,63,5,115,0,0,63,64,5,122,0,0,64,65,5,101,
        0,0,65,66,5,114,0,0,66,67,5,111,0,0,67,18,1,0,0,0,68,69,5,40,0,0,
        69,20,1,0,0,0,70,71,5,41,0,0,71,22,1,0,0,0,72,74,7,0,0,0,73,72,1,
        0,0,0,74,75,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,
        78,6,11,0,0,78,24,1,0,0,0,2,0,75,1,6,0,0
    ]

class UntypedExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    IF = 3
    THEN = 4
    ELSE = 5
    ZERO = 6
    SUCC = 7
    PRED = 8
    ISZERO = 9
    LPAREN = 10
    RPAREN = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'if'", "'then'", "'else'", "'0'", "'succ'", 
            "'pred'", "'iszero'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "IF", "THEN", "ELSE", "ZERO", "SUCC", "PRED", 
            "ISZERO", "LPAREN", "RPAREN", "WS" ]

    ruleNames = [ "TRUE", "FALSE", "IF", "THEN", "ELSE", "ZERO", "SUCC", 
                  "PRED", "ISZERO", "LPAREN", "RPAREN", "WS" ]

    grammarFileName = "UntypedExpr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


