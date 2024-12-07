print("Welcome to the Basic Quiz!")

# Quiz data: Questions, options, and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": {'a': 'Paris', 'b': 'London', 'c': 'Berlin', 'd': 'Rome'},
        "answer": 'a'
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": {'a': 'Earth', 'b': 'Mars', 'c': 'Jupiter', 'd': 'Saturn'},
        "answer": 'c'
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": {'a': 'Charles Dickens', 'b': 'William Shakespeare', 'c': 'Mark Twain', 'd': 'J.K. Rowling'},
        "answer": 'b'
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": {'a': '90', 'b': '100', 'c': '110', 'd': '120'},
        "answer": 'b'
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": {'a': 'Oxygen', 'b': 'Gold', 'c': 'Silver', 'd': 'Helium'},
        "answer": 'a'
    },
    {
        "question": "What is the square root of 64?",
        "options": {'a': '6', 'b': '7', 'c': '8', 'd': '9'},
        "answer": 'c'
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": {'a': 'China', 'b': 'Japan', 'c': 'Thailand', 'd': 'India'},
        "answer": 'b'
    },
    {
        "question": "What is the chemical formula for water?",
        "options": {'a': 'H2O', 'b': 'O2', 'c': 'CO2', 'd': 'H2SO4'},
        "answer": 'a'
    }
]

# Initialize score
score = 0

# Quiz loop
for idx, item in enumerate(quiz_data, start=1):
    print(f"\nQuestion {idx}: {item['question']}")
    for key, value in item['options'].items():
        print(f"{key}) {value}")
    
    inp = input("Enter your answer (a, b, c, or d): ").lower()
    if inp in item['options']:
        print(f"Your answer: {item['options'][inp]}")
        print(f"Correct answer: {item['options'][item['answer']]}")
        if inp == item['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    else:
        print("Invalid selection. No points awarded.")
        print(f"The correct answer was: {item['options'][item['answer']]}")

# Display final score
print("\nQuiz Completed!")
print(f"Your final score: {score}/{len(quiz_data)}")

if score == len(quiz_data):
    print("Perfect score! Amazing job!")
elif score >= len(quiz_data) / 2:
    print("Good effort! Keep it up.")
else:
    print("Better luck next time!")