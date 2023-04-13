"""
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).


second column now means the outcome of the round:
    X = lose (+0)
    Y = draw (+3)
    Z = win (+6)

    rock(1)(A)
    paper(2)(B)
    scissors(3)(C)


"""

score = 0

with open("CODE/Python/AdventOfCode/day two/input.txt", "r+") as f:
    for line in f:
        rounds = line
        if rounds == "A X\n":
            score = 3 + 0 + score
        elif rounds == "A Y\n":
            score = 1 + 3 + score
        elif rounds == "A Z\n":
            score = 2 + 6 + score
        elif rounds == "B X\n":
            score = 1 + 0 + score
        elif rounds == "B Y\n":
            score = 2 + 3 + score
        elif rounds == "B Z\n":
            score = 3 + 6 + score
        elif rounds == "C X\n":
            score = 2 + 0 + score
        elif rounds == "C Y\n":
            score = 3 + 3 + score
        elif rounds == "C Z\n":
            score = 1 + 6 + score


print(score)
