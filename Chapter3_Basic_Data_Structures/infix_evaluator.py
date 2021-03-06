# A program to convert a provided infix expression into a postfix expression
# And calculate its total value
from pythonds.basic import Stack


def main():
    """Serves as the main menu and driver function"""
    while True:
        print("\n~~~Welcome to the Python Infix Evaluation Calculator~~~")
        choice = input('Would you like to proceed?(Y/N): ')
        if choice.title() == 'Y':
            expression, original = grab_input()
            converted = infixToPostfix(expression)
            print(converted)
            evaluated = postfixEval(converted)
            show_results(original, converted, evaluated)
            continue

        elif choice.title() == 'N':
            print("Closing program...")
            break

        else:
            print("Invalid input. Returning to main...")


def grab_input():
    """A function to collect and screen user input to prevent errors"""
    while True:
        prompt = ("\nPlease enter an appropriate infix arithmetic expression (using numbers).")
        prompt += ("\nEnsure to separate each character by a space: ")
        infexexpr = input(prompt)

        # Splitting user string into a list
        tokenList = infexexpr.split()

        # Creating incrementors to count number of parentheses, operators, and operands
        inc1, inc2, inc3, inc4 = (0, 0, 0, 0)
        operator_list = ['+', '-', '*', '/']

        # Looping through input list to record numbers of each component
        for token in tokenList:
            if token == '(':
                inc1 += 1
            elif token == ')':
                inc2 += 1
            elif token in operator_list:
                inc3 += 1
            elif token in '0123456789':
                inc4 += 1
            elif token == " ":
                continue
            else:
                print("The character " + token + " is invalid.")
                break

        if inc1 == inc2 and (inc4 - inc3) == 1:
            return tokenList, infexexpr
        else:
            print("\nError detected in input string.")
            print("Please ensure that all parentheses are closed")
            print("and that the number of operators is one less than the number of operands.")

            choice = input("Try again?(Y/N): ")
            if choice.title() == 'Y':
                continue
            else:
                return


def infixToPostfix(tokenList):
    """Converts an infix arithmetic expression to postfix"""

    # Creating a dictionary to hold oprator precedence
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack()
    postfixList = []

    for token in tokenList:
        # Adding any operands to the postFix list
        if token in "0123456789":
            postfixList.append(token)

        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty() and (prec[opStack.peek()] >= prec[token])):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


def postfixEval(tokenList):
    """Arithmentically evaluates the result of a postfix expression"""
    operandStack = Stack()

    tokenList = tokenList.split()

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            print(operand2)
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


def show_results(original, converted, evaluated):
    """A function to print the original infix expression and the converted postfix expression"""
    print("\nThe original infix expression was :" + str(original))
    print("The postfix equivalent of the expression was: " + str(converted))
    print("The numerical value of the infix expression is: " + str(evaluated))


main()
