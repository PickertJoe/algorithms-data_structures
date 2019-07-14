# infixToPostfix duplicated from Miller and Ranum's text
# My contribution was to add a feature that accounts for user input error
# Also created a driver function to make the program usable

from pythonds.basic import Stack
import string


def main():
    """Serves as the main menu and driver function"""
    while True:
        print("\n~~~Welcome to the Python Infix to Postfix Converter~~~")
        choice = input('Would you like to proceed?(Y/N): ')
        if choice.title() == 'Y':
            expression, original = grab_input()
            converted = infixToPostfix(expression)
            show_results(original, converted)
            continue

        elif choice.title() == 'N':
            print("Closing program...")
            break

        else:
            print("Invalid input. Returning to main...")


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
        prompt = ("\nPlease enter an appropriate infix arithmetic expression (using letters).")
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
            elif token in string.ascii_uppercase:
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


def show_results(expression, converted):
    """A function to print the original infix expression and the converted postfix expression"""
    print("\nThe original infix expression was :" + str(expression))
    print("The converted postfix expression is: " + str(converted))


main()
