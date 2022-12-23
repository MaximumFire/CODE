lines = []

with open("CODE/Python/AdventOfCode/day 1/input.txt", "r+") as f:
    temp = []
    for line in f.readlines():
        if line != "\n":
            temp.append(int(line[:len(line)-1]))
        else:
            lines.append(sum(temp))
            temp = []

total = max(lines)
lines.remove(max(lines))

total += max(lines)
lines.remove(max(lines))

total += max(lines)
print(total)