def school_age_calc(age, name):
    if age < 5:
        return f"{name} is only {age} years old, too young for school."
    elif 5 <= age <= 18:
        return f"{name} is {age} years old and of school age."
    else:
        return f"{name} is not of school age."

# Ask for name
name = input("Enter the child's name: ")

# Ask for age with validation
while True:
    age_input = input("Enter the child's age (or 'q' to quit): ")
    if age_input.lower() == "q":
        print("Program closed. Goodbye!")
        break
    try:
        age = int(age_input)
        message = school_age_calc(age, name)
        print(message)
        break   # exit loop once valid age is entered
    except ValueError:
        print("Invalid age entered. Please enter a number.\n")
