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
        if ast.FuncKind == AST.FuncKind.SUCC:
            return current_value + 1
        elif ast.FuncKind == AST.FuncKind.PRED:
            return current_value - 1
        elif ast.FuncKind == AST.FuncKind.PAREN:
            return current_value
        else:
            return current_value == 0
