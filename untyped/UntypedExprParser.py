# Generated from ./UntypedExpr.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,25,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,23,8,0,1,0,0,0,1,0,0,0,30,
        0,22,1,0,0,0,2,23,5,2,0,0,3,23,5,1,0,0,4,23,5,6,0,0,5,6,5,3,0,0,
        6,7,3,0,0,0,7,8,5,4,0,0,8,9,3,0,0,0,9,10,5,5,0,0,10,11,3,0,0,0,11,
        23,1,0,0,0,12,13,5,7,0,0,13,23,3,0,0,0,14,15,5,8,0,0,15,23,3,0,0,
        0,16,17,5,9,0,0,17,23,3,0,0,0,18,19,5,10,0,0,19,20,3,0,0,0,20,21,
        5,11,0,0,21,23,1,0,0,0,22,2,1,0,0,0,22,3,1,0,0,0,22,4,1,0,0,0,22,
        5,1,0,0,0,22,12,1,0,0,0,22,14,1,0,0,0,22,16,1,0,0,0,22,18,1,0,0,
        0,23,1,1,0,0,0,1,22
    ]

class UntypedExprParser ( Parser ):

    grammarFileName = "UntypedExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'if'", "'then'", 
                     "'else'", "'0'", "'succ'", "'pred'", "'iszero'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "IF", "THEN", "ELSE", 
                      "ZERO", "SUCC", "PRED", "ISZERO", "LPAREN", "RPAREN", 
                      "WS" ]

    RULE_term = 0

    ruleNames =  [ "term" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    IF=3
    THEN=4
    ELSE=5
    ZERO=6
    SUCC=7
    PRED=8
    ISZERO=9
    LPAREN=10
    RPAREN=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return UntypedExprParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UntypedExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(UntypedExprParser.LPAREN, 0)
        def term(self):
            return self.getTypedRuleContext(UntypedExprParser.TermContext,0)

        def RPAREN(self):
            return self.getToken(UntypedExprParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class SuccContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UntypedExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUCC(self):
            return self.getToken(UntypedExprParser.SUCC, 0)
        def term(self):
            return self.getTypedRuleContext(UntypedExprParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSucc" ):
                return visitor.visitSucc(self)
            else:
                return visitor.visitChildren(self)


    class PredContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UntypedExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRED(self):
            return self.getToken(UntypedExprParser.PRED, 0)
        def term(self):
            return self.getTypedRuleContext(UntypedExprParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPred" ):
                return visitor.visitPred(self)
            else:
                return visitor.visitChildren(self)


    class IsZeroContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UntypedExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISZERO(self):
            return self.getToken(UntypedExprParser.ISZERO, 0)
        def term(self):
            return self.getTypedRuleContext(UntypedExprParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsZero" ):
                return visitor.visitIsZero(self)
            else:
                return visitor.visitChildren(self)


    class ConstZeroContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UntypedExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZERO(self):
            return self.getToken(UntypedExprParser.ZERO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstZero" ):
                return visitor.visitConstZero(self)
            else:
                return visitor.visitChildren(self)


    class ConstFalseContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UntypedExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(UntypedExprParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstFalse" ):
                return visitor.visitConstFalse(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UntypedExprParser.TermContext
            super().__init__(parser)
            self.condition = None # TermContext
            self.thenBranch = None # TermContext
            self.elseBranch = None # TermContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(UntypedExprParser.IF, 0)
        def THEN(self):
            return self.getToken(UntypedExprParser.THEN, 0)
        def ELSE(self):
            return self.getToken(UntypedExprParser.ELSE, 0)
        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UntypedExprParser.TermContext)
            else:
                return self.getTypedRuleContext(UntypedExprParser.TermContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class ConstTrueContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UntypedExprParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(UntypedExprParser.TRUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstTrue" ):
                return visitor.visitConstTrue(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = UntypedExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_term)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = UntypedExprParser.ConstFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                self.match(UntypedExprParser.FALSE)
                pass
            elif token in [1]:
                localctx = UntypedExprParser.ConstTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 3
                self.match(UntypedExprParser.TRUE)
                pass
            elif token in [6]:
                localctx = UntypedExprParser.ConstZeroContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 4
                self.match(UntypedExprParser.ZERO)
                pass
            elif token in [3]:
                localctx = UntypedExprParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 5
                self.match(UntypedExprParser.IF)
                self.state = 6
                localctx.condition = self.term()
                self.state = 7
                self.match(UntypedExprParser.THEN)
                self.state = 8
                localctx.thenBranch = self.term()
                self.state = 9
                self.match(UntypedExprParser.ELSE)
                self.state = 10
                localctx.elseBranch = self.term()
                pass
            elif token in [7]:
                localctx = UntypedExprParser.SuccContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 12
                self.match(UntypedExprParser.SUCC)
                self.state = 13
                self.term()
                pass
            elif token in [8]:
                localctx = UntypedExprParser.PredContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 14
                self.match(UntypedExprParser.PRED)
                self.state = 15
                self.term()
                pass
            elif token in [9]:
                localctx = UntypedExprParser.IsZeroContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 16
                self.match(UntypedExprParser.ISZERO)
                self.state = 17
                self.term()
                pass
            elif token in [10]:
                localctx = UntypedExprParser.ParenContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 18
                self.match(UntypedExprParser.LPAREN)
                self.state = 19
                self.term()
                self.state = 20
                self.match(UntypedExprParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





