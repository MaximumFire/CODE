with open("CODE/Python/AdventOfCode/2023/Day 4/Part 1/input.txt", "r") as f:
    data = f.readlines()

copies = [1 for i in range(len(data))]
# vals = [0 for i in range(len(data))]

for i in range(len(data)):
    x = data[i].find(":")
    data[i] = data[i][x+2:].strip("\n").split(" | ")
    data[i] = [x.split(" ") for x in data[i]]
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            if data[i][j][k].isnumeric():
                data[i][j][k] = int(data[i][j][k])

def findMatches(line):
    print(line)
    matches = 0
    for i in range(len(line[0])):
        if line[0][i] in line[1] and line[0][i] != "":
            matches += 1
    return matches

def setCopies(n, matches):
    for i in range(n+1, n+matches+1):
        if i < len(copies):
            copies[i] += copies[n]
        else:
            return

for i in range(len(data)):
    matches = findMatches(data[i])
    print(matches)
    setCopies(i, matches)
    # for j in range(matches):
    #     if vals[i] == 0:
    #         vals[i] = 1
    #     else:
    #         vals[i] *= 2

t = 0
for i in range(len(copies)):
    if copies[i] != 0:
        t += copies[i]

print(copies)
print(t)
# print(vals)