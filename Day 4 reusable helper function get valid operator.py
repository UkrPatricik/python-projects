def get_valid_operator(prompt, valid_ops=None):
    """
    Prompt the user for an operator.
    - Keeps asking until a valid operator is entered.
    - Default valid operators: +, -, *, /, **, %
    - User can type 'q' to quit.
    """
    if valid_ops is None:
        valid_ops = {"+", "-", "*", "/", "**", "%"}

    while True:
        op = input(prompt)
        if op.lower() == "q":
            print("Program closed. Goodbye!")
            quit()
        if op in valid_ops:
            return op
        else:
            print(f"Invalid operator. Please enter one of: {', '.join(valid_ops)}.\n")
