#this function calc will help determine if a child is of school age

def school_age_calc(age, name):
    if age < 5:
        print(f"{name} is only {age} years old, too young for school.")
    elif age >= 5 and age <= 18:
        print(f"{name} is {age} years old and of school age.")
    else:
        print(f"{name} is not of school age.")

print(school_age_calc(22, "Alice"))

