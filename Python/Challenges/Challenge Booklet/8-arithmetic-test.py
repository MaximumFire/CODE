#Arithmetic Test Generator
import random as r

real_answers = []
student_answers = []

def getQuestion(type):
    global real_answers
    if type == "add":
        min = r.randint(1, 49)
        max = r.randint(50, 99)
        num1 = r.randint(min, max)
        num2 = r.randint(min, max)
        answer = num1 + num2
        real_answers.append(answer)
        return f"{num1} + {num2}"
    elif type == "sub":
        min = r.randint(1, 49)
        max = r.randint(50, 99)
        num1 = r.randint(min, max)
        num2 = r.randint(min, max)
        answer = num1 - num2
        real_answers.append(answer)
        return f"{num1} - {num2}"
    elif type == "mul":
        min = r.randint(1, 49)
        max = r.randint(50, 99)
        num1 = r.randint(min, max)
        num2 = r.randint(min, max)
        answer = num1 * num2
        real_answers.append(answer)
        return f"{num1} * {num2}"
    elif type == "div":
        while True:
            min = r.randint(1, 49)
            max = r.randint(50, 99)
            num1 = r.randint(min, max)
            num2 = r.randint(min, max)
            answer = num1 / num2
            if answer.is_integer():
                break
            else:
                continue
        real_answers.append(answer)
        return f"{num1} / {num2}"

no_of_questions = int(input("How many questions should the test have? "))
name = input("Enter a name? ")
counter = 0
options = ["add", "sub", "mul", "div"]
score = 0
time = 0
active = True
seconds = None
minutes = None
for i in range(no_of_questions):
    print(f"Question {counter+1}:")
    print(getQuestion(r.choice(options)))
    answer = int(input("What is your answer? "))
    if real_answers[counter] == answer:
        print("Well done! That was correct!")
        score += 1
    else:
        print("Something was incorrect there.")
    counter += 1
print(f"Name: {name}, Score: {score},Number of questions: {no_of_questions}, Time: {minutes}Mins {seconds}Secs")