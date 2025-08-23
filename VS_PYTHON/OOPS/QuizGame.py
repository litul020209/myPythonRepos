# def question():
#     Q=["what is the chemical name of water ? ", "Total bones in human body is ?", "Sun is a what ? ","(a+b) power 2 formula is what ? ", "Capital of India is ? "]
#     # for i in len(Q):
#     #     for j in (i+1):
#     #         return j
#     # return j 


# def ans():
#      pass

# def mark():

#     pass

# def percentage():
#     pass



# A=["H2O","HOO2","OH2H2","H2O2"]
# B=[202,205,210,206]
# C=["Nebula" ,"Moon" ,"Planet","Star"]
# D=["a2+b2+2(a+b)","(a+b)-(a+b)" ,"a+b(a*b)","(a+b+b+a)"]
# E=["Mumbai","Delhi","Hyderbad","Bengalur"]
# print(question())



# Step 1: Create a list of questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A"
    },
    {
        "question": "Who wrote the Indian national anthem?",
        "options": ["A. Mahatma Gandhi", "B. Rabindranath Tagore", "C. Nehru", "D. Subhash Chandra Bose"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    }
]

# Step 2: Initialize score
score = 0

# Step 3: Loop through each question
for q in questions:
    print("\n" + q["question"])          # Print the question
    for option in q["options"]:          # Print all 4 options
        print(option)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()  # Ask for user input and format it
    
    if user_answer == q["answer"]:       # Check if the answer is correct
        print("Correct! ✅")
        score += 1                       # Add 1 to score
    else:
        print(f"Wrong ❌! Correct answer is {q['answer']}")

# Step 4: Print the final score
print(f"\nYour Final Score is {score} out of {len(questions)} 🎯")
