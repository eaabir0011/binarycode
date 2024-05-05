import json

# Function to load questions from a JSON file
def load_questions():
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)
    except FileNotFoundError:
        questions = []
    return questions

# Function to save questions to a JSON file
def save_questions(questions):
    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=2)

# Function to add a new question
def add_question():
    question_text = input("Enter the question: ")
    options = input("Enter the options separated by commas: ").split(",")
    correct_option = input("Enter the correct option: ")

    question = {
        "question": question_text,
        "options": options,
        "correct_option": correct_option.strip(),
    }

    questions = load_questions()
    questions.append(question)
    save_questions(questions)
    print("Question added successfully!")

# Function to display questions
def display_questions():
    questions = load_questions()
    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question['question']}")
        print(f"   Options: {', '.join(question['options'])}")
        print()

# Function for user login
def user_login():
    password = input("Enter your password: ")
    # Add your own password validation logic here
    return password == "1234"

# Function for user to answer questions
def answer_questions():
    if not user_login():
        print("Invalid password. Exiting.")
        return

    display_questions()
    questions = load_questions()
    score = 0

    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the option number): ").strip()

        if user_answer == question["correct_option"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['correct_option']}.")

    print(f"Your final score is: {score}/{len(questions)}")

# Main menu
while True:
    print("\n=== MCQ Program ===")
    print("1. Add a new question")
    print("2. Answer questions")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_question()
    elif choice == "2":
        answer_questions()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
