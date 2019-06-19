# postfixEval duplicated rom Miller and Ranum's text
# My contribution was to add a feature that accounts for user input error
# Also created a driver function to make the program usable

from pythonds.basic import Stack


def main():
    """Serves as the main menu and driver function"""
    while True:
        print("\n~~~Welcome to the Python Postfix Evaluation Calculator~~~")
        choice = input('Would you like to proceed?(Y/N): ')
        if choice.title() == 'Y':
            expression, original = grab_input()
            converted = postfixEval(expression)
            show_results(original, converted)
            continue

        elif choice.title() == 'N':
            print("Closing program...")
            break

        else:
            print("Invalid input. Returning to main...")


def postfixEval(tokenList):
    """Arithmentically evaluates the result of a postfix expression"""
    operandStack = Stack()

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


def grab_input():
    """A function to collect and screen user input to prevent errors"""
    while True:
        prompt = ("\nPlease enter an appropriate postfix arithmetic expression.")
        prompt += ("\nEnsure to separate each character by a space")
        prompt += ("\nAnd use only numbers and arithmetic operators: ")
        postfixexpr = input(prompt)

        # Splitting user string into a list
        tokenList = postfixexpr.split()
        # Creating incrementors to count number of parentheses, operators, and operands
        inc1, inc2 = (0, 0)
        operator_list = ['+', '-', '*', '/']
        # A flag to activate if an invalid character is encountered in the input string
        flag = False

        # Looping through input list to record numbers of each component
        for token in tokenList:
            if token in operator_list:
                inc1 += 1
            elif token in '0123456789':
                inc2 += 1
            elif token == " ":
                continue
            else:
                print("The character " + token + " is invalid.")
                flag = True

        if (inc2 - inc1) == 1 and flag is True:
            return tokenList, postfixexpr
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
    print("\nThe original postfix expression was :" + str(expression))
    print("The calculated value of the expression is: " + str(converted))


main()
