"""
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

score = 0
# translations = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
# winning = [["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"]]
# drawing = [["rock", "rock"], ["paper", "paper"], ["scissors", "scissors"]]
# scores = {"rock": 1, "paper": 2, "scissors": 3}

with open("CODE/Python/AdventOfCode/day two/input.txt", "r+") as f:
    for line in f:
        rounds = line
        if rounds == "A X\n":
            score = 3 + 1 + score
        elif rounds == "A Y\n":
            score = 6 + 2 + score
        elif rounds == "A Z\n":
            score = 0+3+score
        elif rounds == "B X\n":
            score = 0 + 1 + score
        elif rounds == "B Y\n":
            score = 3 + 2 + score
        elif rounds == "B Z\n":
            score = 6 + 3 + score
        elif rounds == "C X\n":
            score = 6 + 1 + score
        elif rounds == "C Y\n":
            score = 0 + 2 + score
        elif rounds == "C Z\n":
            score = 3 + 3 + score


print(score)
