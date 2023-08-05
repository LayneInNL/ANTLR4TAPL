from exprast import *


def eval(ast):
    if isinstance(ast, ConstTerm):
        return ast.value
    elif isinstance(ast, IfTerm):
        res = eval(ast.condition)
        if res:
            return eval(ast.thenBranch)
        else:
            return eval(ast.elseBranch)
    else:
        current_value = eval(ast.value)
        if ast.kind == FuncKind.SUCC:
            return current_value + 1
        elif ast.kind == FuncKind.PRED:
            return current_value - 1
        elif ast.kind == FuncKind.PAREN:
            return current_value
        else:
            return current_value == 0
