questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["2", "3", "4", "5"],
        "answer": "4"
    },
    {
        "question": "What is 3 + 3?",
        "options": ["4", "5", "6", "7"],
        "answer": "6"
    },
    {
        "question": "What is 5 + 5?",
        "options": ["8", "9", "10", "11"],
        "answer": "10"
    },
    {
        "question": "What is 10 - 4?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "What is 7 * 3?",
        "options": ["20", "21", "22", "23"],
        "answer": "21"
    }
]

score = 0

for question in questions:
    print(question["question"])

    for number, option in enumerate(question["options"], start=1):
        print(f"{number}. {option}")

    choice = 0

    while choice < 1 or choice > 4:
        choice = int(input("Choose an answer (1-4): "))

        if choice < 1 or choice > 4:
            print("Invalid choice. Try again.")

    selected_option = question["options"][choice - 1]

    if selected_option == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"Your score is: {score}/{len(questions)}")
