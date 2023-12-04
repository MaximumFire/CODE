with open("CODE/Python/AdventOfCode/2023/Day 1/Part 1/input.txt", "r") as f:
    lines = f.readlines()

ints = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

total = 0
for line in lines:
    val = ""
    for i in range(0, len(line), 1):
        if line[i] in ints:
            val += line[i]
            break
    for i in range(len(line) - 1, -1, -1):
        if line[i] in ints:
            val += line[i]
            break
    total += int(val)

print(total)
