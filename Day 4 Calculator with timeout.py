import signal
import sys

# ===== Timeout setup (macOS/Linux) =====
TIMEOUT_SECS = 60  # <- adjust to taste

def _timeout_handler(signum, frame):
    print("\nNo activity detected. Calculator closed due to timeout.")
    sys.exit(0)

signal.signal(signal.SIGALRM, _timeout_handler)
# =======================================


def get_valid_number(prompt, min_value=None, max_value=None):
    """
    Prompt the user for a number.
    - Keeps asking until valid input is entered.
    - Optional min/max bounds.
    - 'q' quits the program cleanly.
    - Returns float.
    """
    while True:
        # reset inactivity timer right before we ask
        signal.alarm(TIMEOUT_SECS)
        value = input(prompt)

        if value.lower() == "q":
            print("Calculator closed. Goodbye!")
            signal.alarm(0)  # cancel timer
            sys.exit(0)

        try:
            num = float(value)
            if min_value is not None and num < min_value:
                print(f"Value must be at least {min_value}. Please try again.\n")
                continue
            if max_value is not None and num > max_value:
                print(f"Value must be at most {max_value}. Please try again.\n")
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def get_valid_operator(prompt, valid_ops=None):
    """
    Prompt the user for an operator.
    - Keeps asking until a valid operator is entered.
    - Default valid operators: +, -, *, /, **, %
    - 'q' quits the program cleanly.
    """
    if valid_ops is None:
        valid_ops = {"+", "-", "*", "/", "**", "%"}

    while True:
        # reset inactivity timer right before we ask
        signal.alarm(TIMEOUT_SECS)
        op = input(prompt)

        if op.lower() == "q":
            print("Calculator closed. Goodbye!")
            signal.alarm(0)  # cancel timer
            sys.exit(0)

        if op in valid_ops:
            return op
        else:
            print(f"Invalid operator. Please enter one of: {', '.join(valid_ops)}.\n")


print("Simple Calculator (Refactored, with timeout)")
print("Type 'q' at any time to quit.")
print(f"(Auto-timeout after {TIMEOUT_SECS} seconds of inactivity.)")
print("Note: Results are rounded to 2 decimal places.")
print("Operators supported: +, -, *, /, ** (power), % (modulus)\n")

try:
    while True:
        num1 = get_valid_number("Enter first number (or 'q' to quit): ")
        op   = get_valid_operator("Enter operator (+, -, *, /, **, %) or 'q' to quit: ")
        num2 = get_valid_number("Enter second number (or 'q' to quit): ")

        # Compute with safety checks
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: Division by zero\n")
                continue
            result = num1 / num2
        elif op == "**":
            result = num1 ** num2
        elif op == "%":
            if num2 == 0:
                print("Error: Modulus by zero\n")
                continue
            result = num1 % num2

        print("Result:", round(result, 2), "\n")

finally:
    # Make sure the alarm is turned off if the program exits normally
    signal.alarm(0)
