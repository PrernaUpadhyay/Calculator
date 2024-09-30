# Define the ASCII Art for Calculator
calculator_art = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


# Define the basic arithmetic functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary to store the operations and corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# Calculator logic
def calculator():
    print(calculator_art)  # Print the ASCII calculator when the program starts

    should_continue = True
    num1 = float(input("What is the first number?: "))

    while should_continue:
        # Print available operations
        for symbol in operations:
            print(symbol)

        # Choose the operation
        operation_symbol = input("Pick an operation: ")

        # Get the second number
        num2 = float(input("What is the next number?: "))

        # Call the selected function from the dictionary
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        # Display the result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask if the user wants to continue with the current result or start a new calculation
        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            num1 = answer  # Continue with the result as the next starting number
        else:
            should_continue = False
            calculator()  # Start a new calculation


# Start the calculator program
calculator()
