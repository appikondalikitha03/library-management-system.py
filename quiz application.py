import random

# List of questions
quiz = [
    {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "answer": "Gandhi"
    },
    {
        "question": "What is 5 + 7?",
        "answer": "12"
    },
    {
        "question": "Which programming language is known for AI and Data Science?",
        "answer": "Python"
    }
]

score = 0

print("===== QUIZ APPLICATION =====")

for i in range(5):
    q = random.choice(quiz)

    print(f"\nQuestion {i+1}: {q['question']}")
    user_answer = input("Your Answer: ")

    if user_answer.lower() == q["answer"].lower():
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct Answer is:", q["answer"])

print("\n===== QUIZ COMPLETED =====")
print("Your Score:", score, "/ 5")