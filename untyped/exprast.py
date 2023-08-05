from enum import Enum, auto
from UntypedExprVisitor import UntypedExprVisitor


class FuncKind(Enum):
    SUCC = auto()
    PRED = auto()
    ISZERO = auto()
    PAREN = auto()


class AST:
    pass


# represent false, true and zero
class ConstTerm(AST):
    def __init__(self, value) -> None:
        self.value = value


# represent if
class IfTerm(AST):
    def __init__(self, condition, thenBranch, elseBranch) -> None:
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch


# represent succ, pred, iszero and paren
class FuncTerm(AST):
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value


class NodeVisitor(UntypedExprVisitor):
    def visitConstFalse(self, _):
        return ConstTerm(False)

    def visitConstTrue(self, _):
        return ConstTerm(True)

    def visitConstZero(self, _):
        return ConstTerm(0)

    def visitIf(self, ctx):
        condition = self.visit(ctx.condition)
        thenBranch = self.visit(ctx.thenBranch)
        elseBranch = self.visit(ctx.elseBranch)
        return IfTerm(condition, thenBranch, elseBranch)

    def visitSucc(self, ctx):
        result = self.visit(ctx.term())
        return FuncTerm(FuncKind.SUCC, result)

    def visitPred(self, ctx):
        result = self.visit(ctx.term())
        return FuncTerm(FuncKind.PRED, result)

    def visitIsZero(self, ctx):
        result = self.visit(ctx.term())
        return FuncTerm(FuncKind.ISZERO, result)

    def visitParen(self, ctx):
        result = self.visit(ctx.term())
        return FuncTerm(FuncKind.PAREN, result)
