# Code ducplicated rom Miller and Ranum's text

from pythonds.basic import Stack


def postfixEval(postfixExpr):
    """Arithmentically evaluates the result of a postfix expression"""
    operandStack = Stack()

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


def doMath(op, op1, op2):
    """Performs the arithmetic"""
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2
