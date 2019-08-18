# A program that can reverse a user-provided string using recursion


def reverse(string):
    """Prints the reverse of a user-provided string using recursion"""

    # Length of zero is the base case, terminates the reversal function
    if len(string) == 0:
        return

    # Grabbing the first character from the string
    char = string[0]

    # Sending the remainder of the string to the reverse function recursively
    reverse(string[1:])
    print(char, end='')


def main():
    """Driver function for program"""
    while True:
        print("\n~~~Welcome to the Python Recursive String Inverter!~~~")
        string = input("Please enter the string you'd like to reverse: ")
        print("The reverse of " + string + " is ", end='')
        reverse(string)

        continue_choice = input("\n\nWould you like to reverse another string? (Y/N): ")

        if continue_choice.title() == 'N':
            print("Closing program...")
            break
        else:
            continue


main()
