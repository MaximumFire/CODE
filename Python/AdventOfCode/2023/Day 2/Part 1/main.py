with open("CODE/Python/AdventOfCode/2023/Day 2/Part 1/input.txt", "r") as f:
    lines = f.readlines()

total = 0
# 12 red, 13 green, 14 blue
r = 0
g = 0
b = 0

valid = True

for line in lines:
    valid = True
    x = line.find(":")
    line1 = line[x+2:len(line)-1]
    vals = [y.split(", ") for y in line1.split("; ")]
    for i in range(len(vals)):
        r, g, b = 0, 0, 0
        for j in range(len(vals[i])):
            intval = int(vals[i][j].split(" ")[0])
            if vals[i][j].endswith("red"):
                if intval > 12:
                    valid = False
            elif vals[i][j].endswith("green"):
                if intval > 13:
                    valid = False
            elif vals[i][j].endswith("blue"):
                if intval > 14:
                    valid = False
    print(vals, valid)
    if valid:
        total += int(line[5:x])

print(total)