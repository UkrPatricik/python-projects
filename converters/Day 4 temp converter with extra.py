def get_valid_number(prompt, min_value=None, max_value=None):
    """
    Prompt the user for a number.
    Keeps asking until valid input is entered.
    Accepts optional min/max values.
    User can type 'q' to quit.
    """
    while True:
        value = input(prompt)
        if value.lower() == "q":
            print("Program closed. Goodbye!")
            quit()
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


def get_valid_choice(prompt, valid_choices):
    """
    Prompt the user until they enter a valid choice.
    - valid_choices: dict mapping accepted inputs -> normalized label
    - User can type 'q' to quit.
    - Returns the normalized label.
    """
    while True:
        choice = input(prompt).lower().strip()
        if choice == "q":
            print("Program closed. Goodbye!")
            quit()
        if choice in valid_choices:
            return valid_choices[choice]
        else:
            print(f"Invalid choice. Please enter one of: {', '.join(valid_choices.keys())}.\n")


def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


ABS_ZERO_C = -273.15
ABS_ZERO_F = -459.67

VALID_CHOICES = {
    "c→f": "c_to_f", "c->f": "c_to_f", "c": "c_to_f", "cf": "c_to_f",
    "f→c": "f_to_c", "f->c": "f_to_c", "f": "f_to_c", "fc": "f_to_c",
}

print("Temperature Converter")
print("Type 'q' at any time to quit.\n")

while True:
    choice = get_valid_choice("Convert (C→F or F→C)? (type 'q' to quit): ", VALID_CHOICES)

    if choice == "c_to_f":
        print("Formula C→F: (C × 9/5) + 32")
        c = get_valid_number("Enter temperature in Celsius: ", min_value=ABS_ZERO_C)
        f_val = c_to_f(c)
        print(f"Work: ({c} × 9/5) + 32 = {round(f_val, 2)}°F\n")

    elif choice == "f_to_c":
        print("Formula F→C: (F - 32) × 5/9")
        f = get_valid_number("Enter temperature in Fahrenheit: ", min_value=ABS_ZERO_F)
        c_val = f_to_c(f)
        print(f"Work: ({f} - 32) × 5/9 = {round(c_val, 2)}°C\n")
