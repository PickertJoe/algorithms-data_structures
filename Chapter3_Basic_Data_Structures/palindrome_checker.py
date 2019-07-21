# A program to verify whether a given string is a palandrome - Miller and Ranum

from pythonds.basic import Deque


def main():
    while True:
        print("~~~Welcome to the Python Palindrome Checker!~~~")
        palindrome = input("Please enter the string you'd like to test: ")
        tester = palchecker(palindrome)
        if tester is True:
            print("Your input " + palindrome + " is a palindrome!")
        else:
            print("Your input " + palindrome + " is not a palindrome!")

        repeat = input("Would you like to test another?(Y/N)")
        if repeat.title() == 'Y':
            pass
        else:
            break


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        # Removes all spaces from the user's input to ensure that palindrome is detected
        if ch == ' ':
            pass
        else:
            chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        # Ensures palindromes are detected regardless of user capitalization
        if first.title() != last.title():
            stillEqual = False

    return stillEqual


main()
