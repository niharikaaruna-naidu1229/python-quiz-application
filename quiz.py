questions = {
    "1. What is the capital of India?": "a",
    "2. Which language is mainly used for AI?": "b",
    "3. What is 5 + 7?": "c",
    "4. Who wrote 'Romeo and Juliet'?": "a",
    "5. What is the largest planet in our Solar System?": "b",
    "6. What does CPU stand for?": "a",
    "7. Which data type is used for True or False in Python?": "c",
    "8. Which symbol is used to write a comment in Python?": "b",
    "9. What is the output of 2 * 3?": "d",
    "10. Which keyword is used to define a function in Python?": "a"
}


# Options for each question
options = {
    "1. What is the capital of India?": [
        "a) Delhi",
        "b) Mumbai",
        "c) Chennai",
        "d) Kolkata"
    ],

    "2. Which language is mainly used for AI?": [
        "a) C++",
        "b) Python",
        "c) Java",
        "d) Ruby"
    ],

    "3. What is 5 + 7?": [
        "a) 10",
        "b) 11",
        "c) 12",
        "d) 13"
    ],

    "4. Who wrote 'Romeo and Juliet'?": [
        "a) William Shakespeare",
        "b) Charles Dickens",
        "c) J.K. Rowling",
        "d) Mark Twain"
    ],

    "5. What is the largest planet in our Solar System?": [
        "a) Earth",
        "b) Jupiter",
        "c) Saturn",
        "d) Mars"
    ],

    "6. What does CPU stand for?": [
        "a) Central Processing Unit",
        "b) Computer Processing User",
        "c) Central Program Utility",
        "d) Control Processing Unit"
    ],

    "7. Which data type is used for True or False in Python?": [
        "a) String",
        "b) Integer",
        "c) Boolean",
        "d) Float"
    ],

    "8. Which symbol is used to write a comment in Python?": [
        "a) //",
        "b) #",
        "c) /*",
        "d) @"
    ],

    "9. What is the output of 2 * 3?": [
        "a) 5",
        "b) 6.5",
        "c) 9",
        "d) 6"
    ],

    "10. Which keyword is used to define a function in Python?": [
        "a) def",
        "b) function",
        "c) fun",
        "d) define"
    ]
}


# Score
score = 0


# Quiz loop
print("================================")
print("       🧠 PYTHON QUIZ APP")
print("================================")
print("Answer the following 10 questions.")
print("Enter only a, b, c, or d.\n")


for q in questions:

    print(q)

    for opt in options[q]:
        print(opt)

    answer = input("Enter your answer (a/b/c/d): ").lower()

    if answer == questions[q]:

        print("✅ Correct!\n")

        score += 1

    else:

        print(
            f"❌ Wrong! Correct answer is '{questions[q]}'\n"
        )


# Final score
print("================================")
print("          🎯 QUIZ RESULT")
print("================================")

print(
    f"Your final score is: {score} out of {len(questions)}"
)


# Result message
if score == 10:

    print("🏆 Excellent! Perfect Score!")

elif score >= 7:

    print("👏 Great job! Keep learning!")

elif score >= 5:

    print("👍 Good attempt! You can improve!")

else:

    print("💪 Keep practicing and try again!")