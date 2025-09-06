print("Simple Calculator")
print("Type 'q' at any time to quit.\n")

while True:
    num1 = input("Enter first number (or 'q' to quit): ")
    if num1 == "q":
        break
    num1 = float(num1)

    op = input("Enter operator (+, -, *, /) or 'q' to quit: ")
    if op == "q":
        break

    num2 = input("Enter second number (or 'q' to quit): ")
    if num2 == "q":
        break
    num2 = float(num2)

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
    else:
        print("Invalid operator")
    
    print()  # blank line for readability

print("Calculator closed. Goodbye!")
