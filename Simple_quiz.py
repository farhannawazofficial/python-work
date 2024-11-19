print("Welcome to the Quiz Game!")

score = 0

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the chemical symbol for gold?", "Au"),
    ("What is the name of the first person to walk on the moon?", "Neil Armstrong"),
    ("How many bones are in the human body?", "206")
]

for question, answer in questions:
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is", answer)

print("You got", score, "out of", len(questions), "questions correct.")
