print("Simple Calculator")
print("Type 'q' at any time to quit.")
print("Note: Results are rounded to 2 decimal places.\n")

def get_number(prompt):
    """Prompt until the user enters a valid number or 'q' to quit."""
    while True:
        s = input(prompt)
        if s == "q":
            return None, True  # quit
        try:
            return float(s), False
        except ValueError:
            print("Wrong entry, try again.\n")

def get_operator(prompt):
    """Prompt until the user enters a valid operator or 'q' to quit."""
    valid = {"+", "-", "*", "/"}
    while True:
        op = input(prompt)
        if op == "q":
            return None, True  # quit
        if op in valid:
            return op, False
        print("Invalid operator, please enter +, -, * or /.\n")

while True:
    # First number
    num1, quit_flag = get_number("Enter first number (or 'q' to quit): ")
    if quit_flag:
        break

    # Operator
    op, quit_flag = get_operator("Enter operator (+, -, *, /) or 'q' to quit: ")
    if quit_flag:
        break

    # Second number
    num2, quit_flag = get_number("Enter second number (or 'q' to quit): ")
    if quit_flag:
        break

    # Compute
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    else:  # op == "/"
        if num2 == 0:
            print("Error: Division by zero\n")
            continue
        result = num1 / num2

    # Round and print
    print("Result:", round(result, 2), "\n")

print("Calculator closed. Goodbye!")
