#Quiz Game using python 

questions = ("What is the boiling point of water at sea level?",
             "Which gas do plants absorb from the atmosphere during photosynthesis?",
             "Which planet is known as the 'Red Planet'?",
             " What is H₂O commonly known as?",
             " Which planet is known for its beautiful rings?"
)




options = (("A. 100°C", "B. 0°C", "C. 50°C", "D. 25°C"),
           ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"),
           ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
           ("A. Water", "B. Salt", "C. Sugar", "D. Alcohol"),
           ("A. Venus", "B. Saturn", "C. Jupiter", "D. Neptune")
           )


answers = ("A", "B", "C", "A", "B")

guesses = []
score = 0
question_number = 0


for question in questions:
    print("--------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter A , B , C , D ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("correct!")
    else: 
        print("incorrect")
        print(f"{answers[question_number]} is the correct answer")
    question_number += 1

print("--------------------------------------")
print("    Quiz results ")
print("--------------------------------------")

print("Answers : ",end="")
for answer in answers:
    print(answer,end = "")
print()

print("Guesses : ",end ="")
for guess in guesses:
    print(guess,end="")
print()

score = int(score / len(questions) *100)
print(f"your score is {score}%")
