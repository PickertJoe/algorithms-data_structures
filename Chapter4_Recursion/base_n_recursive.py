
from stack_class import Stack

bStack = Stack()


def toStr(n, base):
    """This function converts a given integer into a string version of its base n companion"""
    convertString = '0123456789ABCDEF'
    if n < base:
        bStack.push(convertString[n])
    else:
        bStack.push(convertString[n % base])
        toStr(n // base, base)

    output = []
    while not bStack.isEmpty():
        output.append(bStack.pop())

    return ' '.join(output)
