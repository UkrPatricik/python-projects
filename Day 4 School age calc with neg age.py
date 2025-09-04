def school_age_calc(age, name):
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

            # NEW: Check for negative age
            if age < 0:
                print("Invalid age entered. Age cannot be negative. Please try again.\n")
                continue  # go back and ask again

            message = school_age_calc(age, name)
            print(message + "\n")
            break   # exit inner loop after valid age

        except ValueError:
            print("Invalid age entered. Please enter a number.\n")
            