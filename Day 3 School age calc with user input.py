def school_age_calc(age, name):
    if age < 5:
        return f"{name} is only {age} years old, too young for school."
    elif 5 <= age <= 18:
        return f"{name} is {age} years old and of school age."
    else:
        return f"{name} is not of school age."

# Ask user for input
name = input("Enter the child's name: ")
age_input = input("Enter the child's age: ")

# Validate age input
try:
    age = int(age_input)
    message = school_age_calc(age, name)
    print(message)
except ValueError:
    print("Invalid age entered. Please enter a number.")
