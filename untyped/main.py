from antlr4 import *
from UntypedExprLexer import UntypedExprLexer
from UntypedExprParser import UntypedExprParser
from exprast import NodeVisitor
from evaluator import eval


def main(input_content):
    input_stream = InputStream(input_content)
    lexer = UntypedExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = UntypedExprParser(stream)
    cst = parser.term()
    ast = NodeVisitor().visit(cst)
    res = eval(ast)
    print("The final result is", res)


if __name__ == "__main__":
    main("if false then 0 else (succ 0)")
    main("iszero (pred (succ 0))")
