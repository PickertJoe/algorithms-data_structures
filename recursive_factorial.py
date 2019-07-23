# A simple program to calculate the factorial of a given number recursively


def recursive_factorial(number):
    """Calculates the factorial of a given number via recursion"""
    if number == 1 or number == 0:
        return 1
    else:
        return number * recursive_factorial(number - 1)


def main():
    """Driver function for the program"""
    while True:
        print("~~~Welcome to the Python Factorial Calculator!~~~\n")
        print("For a given number, I will calculate its factorial recursively.")
        number = input("What number would you like to use: ")
        number = int(number)
        factorial = recursive_factorial(number)
        print(factorial)


main()
