import random

def ask_question(question, answer):
    user_answer = input(question + " ")
    return user_answer.lower() == answer.lower()

def main():
    questions = {
        # 1. "paris" to "Paris"
        "What is the capital of France?": "Paris",
        # 2. "2 + 2 = 4" to "3 + 3 = 6"
        "What is 3 + 3?": "6",
        "What is the color of the sky?": "blue",
        # 3. "harper lee" to "Harper Lee"
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
        "What is the largest planet in our solar system?": "jupiter"
    }

    score = 0
    question_list = list(questions.keys())
    random.shuffle(question_list)

    for question in question_list:
        if ask_question(question, questions[question]):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    main()