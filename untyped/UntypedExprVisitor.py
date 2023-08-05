# Generated from ./UntypedExpr.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .UntypedExprParser import UntypedExprParser
else:
    from UntypedExprParser import UntypedExprParser

# This class defines a complete generic visitor for a parse tree produced by UntypedExprParser.

class UntypedExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by UntypedExprParser#constFalse.
    def visitConstFalse(self, ctx:UntypedExprParser.ConstFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UntypedExprParser#constTrue.
    def visitConstTrue(self, ctx:UntypedExprParser.ConstTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UntypedExprParser#constZero.
    def visitConstZero(self, ctx:UntypedExprParser.ConstZeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UntypedExprParser#if.
    def visitIf(self, ctx:UntypedExprParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UntypedExprParser#succ.
    def visitSucc(self, ctx:UntypedExprParser.SuccContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UntypedExprParser#pred.
    def visitPred(self, ctx:UntypedExprParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UntypedExprParser#isZero.
    def visitIsZero(self, ctx:UntypedExprParser.IsZeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UntypedExprParser#paren.
    def visitParen(self, ctx:UntypedExprParser.ParenContext):
        return self.visitChildren(ctx)



del UntypedExprParser