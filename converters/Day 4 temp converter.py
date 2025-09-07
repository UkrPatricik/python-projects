def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Temperature Converter")
print("Type 'q' at any time to quit.\n")

while True:
    choice = input("Convert (C→F or F→C)? (type 'q' to quit): ").lower()
    if choice == "q":
        print("Goodbye!")
        break

    if choice == "c→f" or choice == "c":
        print (f"Formula "f"C→F: (C × 9/5) + 32")
        value = input("Enter temperature in Celsius: ")
        try:
            c = float(value)
            print(f"{c}°C = {round(c_to_f(c), 2)}°F\n")
        except ValueError:
            print("Invalid number, try again.\n")

    elif choice == "f→c" or choice == "f":
        value = input("Enter temperature in Fahrenheit: ")
        try:
            f = float(value)
            print(f"{f}°F = {round(f_to_c(f), 2)}°C\n")
        except ValueError:
            print("Invalid number, try again.\n")

    else:
        print("Invalid choice. Please enter 'C→F' or 'F→C'.\n")
