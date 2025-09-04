def school_age_calc(age, name):
    # Guard against impossible ages
    if age < 0:
        return f"{name}: invalid age ({age})."

    if age < 5:
        return f"{name} is only {age} years old, too young for school."
    elif 5 <= age <= 10:
        return f"{name} is {age} years old and should be in primary school."
    elif 11 <= age <= 13:
        return f"{name} is {age} years old and should be in middle school."
    elif 14 <= age <= 18:
        return f"{name} is {age} years old and should be in high school."
    else:
        return f"{name} is not of school age."


print("School Age Calculator")
print("Type 'q' at any time to quit.\n")

while True:
    # Ask for name
    name = input("Enter the child's name (or 'q' to quit): ")
    if name.lower() == "q":
        print("Program closed. Goodbye!")
        break

    # Ask for age with validation
    while True:
        age_input = input("Enter the child's age (or 'q' to quit): ")
        if age_input.lower() == "q":
            print("Program closed. Goodbye!")
            quit()
        try:
            age = int(age_input)
            message = school_age_calc(age, name)
            print(message)   # <- print the returned string
            print()          # blank line for readability
            break            # exit inner loop after valid age
        except ValueError:
            print("Invalid age entered. Please enter a number.\n")
