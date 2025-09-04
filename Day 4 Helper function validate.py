def get_valid_number(prompt, min_value=None, max_value=None):
    """
    Prompt the user for a number.
    - Keeps asking until valid input is entered.
    - Accepts optional min_value and max_value to restrict the range.
    - Returns the valid number as a float.
    - User can type 'q' to quit.
    """
    while True:
        value = input(prompt)
        if value.lower() == "q":
            print("Program closed. Goodbye!")
            quit()
        try:
            number = float(value)
            if min_value is not None and number < min_value:
                print(f"Value must be at least {min_value}. Please try again.\n")
                continue
            if max_value is not None and number > max_value:
                print(f"Value must be at most {max_value}. Please try again.\n")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a number.\n")
