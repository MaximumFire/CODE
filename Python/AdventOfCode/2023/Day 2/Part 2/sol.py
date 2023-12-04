with open("CODE/Python/AdventOfCode/2023/Day 2/Part 1/input.txt", "r") as f:
    lines = f.readlines()

total = 0
# 12 red, 13 green, 14 blue
r = 0 # min vals of each
g = 0
b = 0


for line in lines:
    x = line.find(":")
    line1 = line[x+2:len(line)-1]
    vals = [y.split(", ") for y in line1.split("; ")]
    r, g, b = 0, 0, 0
    for i in range(len(vals)):
        for j in range(len(vals[i])):
            intval = int(vals[i][j].split(" ")[0])
            if vals[i][j].endswith("red"):
                if intval > r:
                    r = intval
            elif vals[i][j].endswith("green"):
                if intval > g:
                    g = intval
            elif vals[i][j].endswith("blue"):
                if intval > b:
                    b = intval
    print(vals)
    total += (r*g*b)

print(total)