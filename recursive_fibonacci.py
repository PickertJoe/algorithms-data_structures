# A program that will produce the fibonacci sequence for n number of iterations using recursion
# This function was a brief experiment and has been abandoned in a broken state


def fibonacci(iterations, number1, number2):
    """A function that prints the fibonacci sequence recursively for n number of iterations"""
    if iterations == 0:
        print("]")
        return
    if number1 == 0:
        print("[0,1,", end='')

    temp = number1 + number2
    print(str(temp), end=',')
    fibonacci(iterations - 1, number2, temp)


def main():
    """Driver function for fibonacci program"""
    while True:
        print("\n\n~~~Welcome to the Recursive Fibonacci machine!~~~")
        print("For a given number of iterations, I can produce the Fibonacci Sequence recursively.")
        iterations = input("How many iterations would you like to generate?: ")

        # Input control to protect function from blowing up
        try:
            int(iterations)
        except ValueError:
            print("\nInvalid input. Please type an integer")
        else:
            iterations = int(iterations)
            if iterations <= 0:
                print("\nInvalid input. Please type a number greater than zero.")
            elif iterations > 100:
                print("\nWoah there, that's a pretty large number! No need to crash your computer.")
                print("How about a number less than 100?")
            else:
                fibonacci(iterations, 0, 1)

        # Allwoing the user to repeat the funciton if desired
        repeat = input("\nWould you like to generate another sequence?(Y/N): ")

        if repeat.title() == "N":
            print("\nClosing program...")
            break
        else:
            continue


main()
