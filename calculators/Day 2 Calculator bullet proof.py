print("Simple Calculator")
print("Type 'q' at any time to quit.\n")

while True:
    # First number
    num1 = input("Enter first number (or 'q' to quit): ")
    if num1 == "q":
        break
    try:
        num1 = float(num1)
    except ValueError:
        print("Wrong entry, try again.\n")
        continue

    # Operator (validated in a loop)
    while True:
        op = input("Enter operator (+, -, *, /) or 'q' to quit: ")
        if op == "q":
            quit_flag = True
            break
        if op in ["+", "-", "*", "/"]:
            quit_flag = False
            break
        else:
            print("Invalid operator, please enter +, -, * or /.")

    if quit_flag:
        break

    # Second number
    num2 = input("Enter second number (or 'q' to quit): ")
    if num2 == "q":
        break
    try:
        num2 = float(num2)
    except ValueError:
        print("Wrong entry, try again.\n")
        continue

    # Perform calculation
    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")

    print()

print("Calculator closed. Goodbye!")
