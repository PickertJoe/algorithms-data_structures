# infexToPostfix duplicated from Miller and Ranum's text
# My contribution was to add a feature that accounts for user input error
# Also created a driver function to make the program usable

from pythonds.basic import Stack
import string


def main():
    """Serves as the main menu and driver function"""
    while True:
        print("~~~Welcome to the Python Infix to Postfix Converter~~~")
        choice = input('Would you like to proceed?(Y/N): ')
        if choice.title() == 'Y':
            expression = grab_input()
            converted = infixToPostfix(expression)
            show_results(expression, converted)
            continue

        elif choice.title() == 'N':
            print("Closing program...")
            break

        else:
            print("Invalid input. Returning to main...")


def infixToPostfix(infexexpr):
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

    tokenList = infexexpr.split()

    for token in tokenList:
        # Adding any operands to the postFix list
        if token in string.ascii_uppercase:
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


def grab_input():
    """A function to collect and screen user input to prevent errors"""
    while True:
        infexexpr = input("Please enter an appropriate infix arithmetic expression: ")
