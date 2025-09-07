def is_even(num):
    return num % 2 == 0

print("Modulus Practice")
print("Type 'q' to quit at any time.\n")

while True:
    value = input("Enter a number to check if it's even or odd (or 'q' to quit): ")
    if value.lower() == "q":
        print("Goodbye!")
        break
    try:
        num = int(value)
        if is_even(num):
            print(f"{num} is even.\n")
        else:
            print(f"{num} is odd.\n")

        # Divisibility test
        divisor_value = input("Enter a divisor to test divisibility (or 'q' to quit): ")
        if divisor_value.lower() == "q":
            print("Goodbye!")
            break
        divisor = int(divisor_value)

        if divisor == 0:
            print("Divisor cannot be zero.\n")
        elif num % divisor == 0:
            print(f"{num} is divisible by {divisor}.\n")
        else:
            print(f"{num} is not divisible by {divisor}.\n")

    except ValueError:
        print("Invalid input, please enter a number.\n")
