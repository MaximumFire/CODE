import random as r
import os
message = """Welcome to Rock, Paper Scissors \nPlease pick from the following options: \n1. Play vs CPU \n2. 2-player game"""
print(message)
choice = int(input())
p1Score = 0
p2Score = 0

if choice == 1:
    players = 1
elif choice == 2:
    players = 2

gameOver = False

def p1Turn():
    global players, rpsChoice
    rpsChoice = input("Choose R, P, S")
    if players == 1:
        cpuTurn()
    else:
        p2Turn()

def cpuTurn():
    global p2Choice
    cpuChoice = r.randint(1, 3)
    if cpuChoice == 1:
        p2Choice = "R"
    elif cpuChoice == 2:
        p2Choice = "P"
    else:
        p2Choice = "S"
    score()

def p2Turn():
    global rpsChoice, p1Score, p2Score, p2Choice
    os.system("cls")
    p2Choice = input("Choose R, P, S")
    score()
    
def score():
    global rpsChoice, p1Score, p2Score, p2Choice
    os.system("cls")
    print("p1: " + rpsChoice + " p2: " + p2Choice)
    if rpsChoice == "R" and p2Choice == "S":
        p1Score += 1
        print("p1 WINS")
    elif rpsChoice == "S" and p2Choice == "R":
        p2Score += 1
        print("p2 WINS")
    elif rpsChoice == "R" and p2Choice == "P":
        p2Score += 1
        print("p2 WINS")
    elif rpsChoice == "P" and p2Choice == "R":
        p1Score += 1
        print("p1 WINS")
    elif rpsChoice == "P" and p2Choice == "S":
        p2Score += 1
        print("p2 WINS")
    elif rpsChoice == "S" and p2Choice == "P":
        p1Score += 1
        print("p1 WINS")

while not gameOver:
    p1Turn()

a = input("A")

