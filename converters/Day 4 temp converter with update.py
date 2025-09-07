def get_valid_choice(prompt, valid_choices):
    """
    Prompt the user until they enter a valid choice.
    - valid_choices should be a dict mapping keys to 'normalized' labels.
    - User can type 'q' to quit.
    - Returns the normalized choice.
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
