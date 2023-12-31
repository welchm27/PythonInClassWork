#!/usr/bin/env python3

def main():
    # A program that prompts a user for two operators and operation (plus or minus)
    # the program then shows the result.
    # The user may enter q to exit the program.
    calc1 = 0.0
    calc2 = 0.0
    operation = ""
    while (calc1 != "q"):
        print("What is the first operator? Or, enter q to quit: ")
        calc1 = input()
        if calc1 == "Q" or "q":
            break
        calc1 = float(calc1)
        print("What is the second operator? Or, enter q to quit: ")
        calc2 = input()
        if calc2 == "Q" or "q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()
        if operation == "+":
            print(str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
        elif operation == '-':
            print(str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
        else:
            print("Not a valid entry. Restarting...")

if __name__ == "__main__":
    main()
