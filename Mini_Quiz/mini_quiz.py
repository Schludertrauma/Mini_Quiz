'''mini_quiz.py'''
'''This script implements a simple console-based quiz game with multiple-choice questions.'''
'''It includes a welcome message, a set of questions, and a scoring system.'''
'''This script is designed only for exercise purposes.'''


def welcome_message():
    import time
    print("Welcome to the Mini Quiz! Please answer the following questions by typing your answers in the console. Let's get started!")
    time.sleep(2)


def questions():
    questions = [
        {
            "question": "What is the capital of Germany?",
            "options": ["A) Munich", "B) Berlin", "C) Frankfurt", "D) Hamburg"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "question": "What is the correct way to create a list in Python?",
            "options": ["A) list = [1, 2, 3]", "B) list = {1, 2, 3}", "C) list = (1, 2, 3)", "D) list = <1, 2, 3>"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["A) Earth", "B) Saturn", "C) Jupiter", "D) Mars"],
            "answer": "D"
        },
        {
            "question": "What is the output of this code: print(3 * \"7\")?",
            "options": ["A) 21", "B) \"21\"", "C) 777", "D) Error"],
            "answer": "C"
        }

    ]
    return questions


def ask_questions(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
        print()  # Print a newline for better readability
    return score


def score_message(score, total):
    print(f"You scored {score} out of {total}.")
    if score == total:
        print("Excellent job! You're a quiz master!")
    elif score >= total / 3:
        print("Good job! You have a solid understanding.")
    else:
        print("Keep trying! Practice makes perfect.")


def main():
    import time
    welcome_message()
    quiz_questions = questions()
    score = ask_questions(quiz_questions)
    time.sleep(1)
    score_message(score, len(quiz_questions))
    time.sleep(1)
    input("Press Enter to exit the quiz. Thank you for participating!")

# define the function to run the quiz


if __name__ == "__main__":
    main()

# this is the main function to start the quiz
