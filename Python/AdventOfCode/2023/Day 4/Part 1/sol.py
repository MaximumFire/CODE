with open("CODE/Python/AdventOfCode/2023/Day 4/Part 1/input.txt", "r") as f:
    data = f.readlines()

total = 0

for line in data:
    x = line.find(":")
    line = line[x+2:]
    line = line.strip("\n")
    line = line.split(" | ")
    line = [x.split(" ") for x in line]
    for i in range(len(line)):
        for j in range(len(line[i])):
            if line[i][j].isdigit():
                line[i][j] = int(line[i][j])

    score = 0
    for i in range(len(line[0])):
        if line[0][i] != "" and line[0][i] in line[1]:
            if score == 0:
                score = 1
            else:
                score *= 2

    total += score

print(total)