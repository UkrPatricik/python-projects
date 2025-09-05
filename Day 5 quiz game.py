def ask_question(question, correct_answer):
    answer = input(question + " ")
    if answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")
        return False

print("Welcome to the Quiz Game!")
print("Type your answer and press Enter.\n")

score = 0

# Example questions
if ask_question("What is 5 + 7?", "12"):
    score += 1
if ask_question("What is the capital of France?", "Paris"):
    score += 1
if ask_question("What color are bananas?", "Yellow"):
    score += 1

print(f"Your final score: {score}/3")
