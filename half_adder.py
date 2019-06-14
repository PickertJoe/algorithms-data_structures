# A program using the circuit class framework to create a half-adder circuit

from circuit_class import *
import pandas as pd


def main():
    while True:
        print("\n~~~Welcome to the Python Half-Adder Program!~~~")
        choice = input("Please select one of the following options: \n1)Enter inputs for A & B\
            \n2)View truth table for half - adder \n3)Exit program\n: ")

        if choice == '3':
            print("So long!")
            break
        elif choice == '2':
            truth_table()
            continue
        else:
            print("Ensure that respective Pin inputs are identical for both components")
            half_adder()
            continue


def truth_table():
    """A function to print all possible permutations for the half-adder"""

    headers = ['INPUTS', 'OUTPUTS']
    d = {'A': [0, 0, 1, 1], 'B': [0, 1, 0, 1], 'SUM': [0, 1, 1, 0], 'CARRY': [0, 0, 0, 1]}
    df = pd.DataFrame.from_dict(data=d)
    # Still needs work to incorporate tiered headers into table
    print(headers)
    print(df.to_string(index=False))


def half_adder():
    """A function to act as the half_adder cirtuit"""

    s = XorGate("Sum")
    sum = s.getOutput()
    c = AndGate("Carry")
    carry = c.getOutput()

    print("Sum: " + str(sum))
    print("Carry: " + str(carry))


main()
